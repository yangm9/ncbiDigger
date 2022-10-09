from selenium.webdriver.chrome.service import Service
NCBI='https://www.ncbi.nlm.nih.gov'
SEVICE=Service(r'/data_backup/software/usr/bin/chromedriver')
#GENOMEINFODICT用于解决某些Key对应的数据缺失问题
SAMPITEMTUPLE=(
    'isolation source','collection date',
    'geographic location','sample type','type-material',
    'metagenome-source','latitude and longitude','depth',
    'isolate','broad-scale environmental context',
    'environmental medium','note'
)
GENOMEINFODICT={
    'strain':None,
    'collection date':None,
    'number of replicons':None,
    'broad-scale environmental context':None,
    'local-scale environmental context':None,
    'geographic location':None,
    'environmental medium':None,
    'investigation type':None,
    'isolation source':None,
    'Isolation Site':None,
    'project name':None,
    'sample name':None,
    'sample type':None,
    'isolate':None,
    'reference for biomaterial':None,
    'isolation and growth condition':None,
    'latitude and longitude':None,
    'depth':None,
    'metagenomic':None,
    'metagenome-source':None,
    'environmental-sample':None,
    'environment':None,
    'type-material':None,
    'temperature':None,
    'note':None,
    '':None
}

PROJITEMTUPLE=('Project Type','Title','Abstract')
PROJINFODICT={
    'Project Type':None,
    'Title':None,
    'Abstract':None,
    '':None
}

InfoDict={
    'Project':PROJITEMTUPLE,
    'Assembly':SAMPITEMTUPLE
}
