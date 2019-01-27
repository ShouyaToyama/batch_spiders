import json
from logging import getLogger

class MyprojectPipeline(object):

    @classmethod
    def from_crawler(cls, crawler):
        # settings.pyから設定内容を取得する
        dir = crawler.settings['OUTPUT_DIR']
        return cls(dir)

    def __init__(self, dir):
        # from_crawlerメソッドから渡されたdirの値を取得する
        self.dir = dir

    def open_spider(self, spider):
        self.logger = getLogger(__name__)
        self.logger.info('='*30 + 'Start ' + spider.name + '='*30)
        self.json_lines = open(
            '{dir}{spider_name}.jl'.format(dir=self.dir, spider_name=spider.name),
            mode='a'
        )

    def close_spider(self, spider):
        self.json_lines.close()
        self.logger.info('='*30 + 'End ' + spider.name + '='*30)

    def process_item(self, item, spider):
        # itemオブジェクトの値をJSON形式で書き込みする
        self.json_lines.write(json.dumps(dict(item), ensure_ascii=False) + '\n')
        return item