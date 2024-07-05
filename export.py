import datetime
import os
import random

import yaml
from jinja2 import Environment, FileSystemLoader

from src import static

template_dir = 'templates'
i18n_dir = 'i18n'
output_base_dir = 'dist'

env = Environment(loader=FileSystemLoader(template_dir))
randomComments = [
    "Why don't programmers like nature? It has too many bugs.",
    "There are only two hard things in Computer Science: cache invalidation and naming things.",
    "Why do programmers prefer dark mode? Because light attracts bugs.",
    "If you find this comment, tell Bob he owes us coffee.",
]

def buildPath(path, isIndex: bool, locale: str):
    if isIndex:
        return path
    if locale == "en":
        return "/" + path
    else:
        return "/" + locale + path

# ローカライズデータの読み込み
def load_translations(locale):
    with open(os.path.join(i18n_dir, f'{locale}.yml'), 'r', encoding='utf-8') as file:
        return yaml.safe_load(file)

# テンプレートのレンダリングと保存
def render_and_save_template(template_name, translations, output_dir):
    template = env.get_template(template_name)
    rendered_content = template.render(**translations, buildpath=buildPath)
    
    # 出力ディレクトリの作成
    os.makedirs(output_dir, exist_ok=True)
    
    # ファイルの保存
    output_file = os.path.join(output_dir, 'index.html')
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(rendered_content)

# メイン処理
def main():
    locales = ['en', 'ja']
    
    for locale in locales:
        translations = load_translations(locale)
        
        templates = [f for f in os.listdir(template_dir) if f.endswith('.html') and f != 'base.html']
        
        for template_file in templates:
            template_name = os.path.splitext(template_file)[0]
            
            if template_file == 'index.html':
                if locale == 'en':
                    translations["randomMsg"] = randomComments[1]
                    translations["commentAuthor"] = "AmaseCocoa"
                    output_dir = output_base_dir
                else:
                    comment = random.choice(randomComments)
                    translations["randomMsg"] = comment
                    if comment == randomComments[1]:
                        translations["commentAuthor"] = "AmaseCocoa"
                    else:
                        translations["commentAuthor"] = random.choice(["Anonymous Programmer", "John Doe"])
                    output_dir = os.path.join(output_base_dir, locale)
                translations["isIndex"] = True
            else:
                comment = random.choice(randomComments)
                translations["randomMsg"] = comment
                if comment == randomComments[1]:
                    translations["commentAuthor"] = "AmaseCocoa"
                else:
                    translations["commentAuthor"] = random.choice(["Anonymous Programmer", "John Doe"])
                if locale == 'en':
                    output_dir = os.path.join(output_base_dir, template_name)
                else:
                    output_dir = os.path.join(output_base_dir, locale, template_name)
                translations["isIndex"] = False
            translations["updatedAt"] = datetime.datetime.now(datetime.UTC).strftime('%Y/%m/%d %H:%M:%S (UTC)')
            render_and_save_template(template_file, translations, output_dir)

if __name__ == '__main__':
    static.copy()
    main()
