#!/usr/bin/env python3
import os
import sys
import re
import copy
from ..configs import chrome #反反爬设置
from ..configs import setConst
from lxml import etree
from selenium import webdriver
from multiprocessing.dummy import Pool
from functools import partial
from selenium.webdriver.common.by import By # 实现规避检测

NCBI=setConst.NCBI
SEVICE=setConst.SEVICE

def projInfo(accession):
    '''
功能：输入BioProject accession number，返回Project信息相关的字典。
步骤：
    1）开启selenium无头浏览器，
    2）得到accession对应的bioproject主页面，
    3）获得具体项目类型、题目和摘要信息。
    '''
    ChromeOpts=chrome.setoption()
    browser=webdriver.Chrome(service=SEVICE,options=ChromeOpts)
    ProjURLs=f"{NCBI}/bioproject/?term={accession}"
    browser.get(ProjURLs)
    pagetext=browser.page_source
    tree=etree.HTML(pagetext)
    TabDict=copy.deepcopy(setConst.PROJINFODICT)
    try:
        TabDict['Project Type']=tree.xpath('//div[@class="Title"]/h2')[0].text
        TabDict['Title']=tree.xpath(f'//div[@class="Title"]/h3')[0].text
        TabDict['Abstract']=tree.xpath(f'//div[@class="Description"]')[0].text
        trs_num=len(tree.xpath('//table[@id="CombinedTable"]/tbody/tr'))
    except IndexError:
        pass
    browser.quit()
    return TabDict

def biosampleInfo(accession):
    ChromeOpts=chrome.setoption()
    browser=webdriver.Chrome(service=SEVICE,options=ChromeOpts)
    TaxaURLs=f"{NCBI}/biosample/{accession}/"
    browser.get(TaxaURLs)
    pagetext=browser.page_source
    tree=etree.HTML(pagetext)
    trs_num=len(tree.xpath('//dd/table/tbody/tr')) #获取表格行数
    TabDict=copy.deepcopy(setConst.GENOMEINFODICT)
    for i in range(trs_num):
        n=str(i+1)
        th=tree.xpath(f'//dd/table/tbody/tr[{n}]/th')[0]
        th_txt=th.text
        td=tree.xpath(f'//dd/table/tbody/tr[{n}]/td')[0]
        tda=td.find('a')
        td_txt=''
        if tda==None:
            td_txt=td.text
        else:
            td_txt=tda.text
        TabDict[th_txt]=td_txt
    browser.quit()
    return TabDict

def genomeInfo(accession):
    """
功能：输入GCF/GCA，返回Sample信息相关的字典。
步骤：
    1）开启selenium无头浏览器，
    2）先得到assembly的对应accession的主页面，
    3）然后点击蓝色的BioSample ID，
    4）爬虫提取该accession的采样信息。
    """
    ChromeOpts=chrome.setoption()
    browser=webdriver.Chrome(service=SEVICE,options=ChromeOpts)
    TaxaURLs=f"{NCBI}/assembly/{accession}/"
    browser.get(TaxaURLs)
    try:
        BioSample_btn=browser.find_element(By.XPATH,"/html/body/div[1]/div[1]/form/div[1]/div[3]/div[2]/div[1]/div[5]/div[1]/div[1]/div[1]/div[1]/dl[1]/dd[4]/a[1]")
    except BaseException:
        return setConst.GENOMEINFODICT 
    BioSample_btn.click()
    pagetext=browser.page_source
    tree=etree.HTML(pagetext)
    trs_num=len(tree.xpath('//dd/table/tbody/tr')) #获取表格行数
    TabDict=copy.deepcopy(setConst.GENOMEINFODICT)
    for i in range(trs_num):
        n=str(i+1)
        th=tree.xpath(f'//dd/table/tbody/tr[{n}]/th')[0]
        th_txt=th.text
        td=tree.xpath(f'//dd/table/tbody/tr[{n}]/td')[0]
        tda=td.find('a')
        td_txt=''
        if tda==None:
            td_txt=td.text
        else:
            td_txt=tda.text
        TabDict[th_txt]=td_txt
    browser.quit()
    return TabDict

def protInfo(accession):
    ChromeOpts=chrome.setoption()
    browser=webdriver.Chrome(service=SEVICE,options=ChromeOpts)
    TaxaURLs=f"{NCBI}/protein/{accession}"
    browser.get(TaxaURLs)
    pagetext=browser.page_source
    tree=etree.HTML(pagetext)
    TabDict=copy.deepcopy(setConst.PROJINFODICT)
    try:
        Keywords=tree.xpath('//*[@id="viewercontent1"]/div/div/pre/text()[4]')[0].split('\n')[1]
        TabDict['Keywords']=re.split(r'\s+',Keywords,1)[1]
        Source=tree.xpath('//*[@id="viewercontent1"]/div/div/pre/text()[4]')[0].split('\n')[2]
        TabDict['Source']=re.split(r'\s+',Source,1)[1]
        TabDict['BioProject']=tree.xpath('//*[@id="viewercontent1"]/div/div/pre/a[1]')[0].text
        TabDict['BioSample']=tree.xpath('//*[@id="viewercontent1"]/div/div/pre/a[2]')[0].text
    except IndexError:
        pass
    browser.quit()
    return TabDict
MethDict={
    "BioProject":projInfo,
    "BioSample":biosampleInfo,
    "Assembly":genomeInfo,
    "Protein":protInfo
}
