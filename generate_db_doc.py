import sys, os, markdown

def setup():
    print('setup generate_db_doc')
    try:
        os.mkdir('input')
        os.mkdir('output')
    except FileExistsError:
        print('Directory already exists')

def md_to_html(input_file_path):
    #ファイルをロード
    print('ファイルをロード')
    output_file = ''
    try:
        with open(f'{input_file_path}', "r") as input_file:
            #マークダウンをhtmlに変換
            input_file = input_file.read()
            output = markdown.markdown(input_file, extensions=['gfm'])
    except FileNotFoundError:
        print(f'{input_file_path} not found')

    #ファイルを置換
    output = output.replace('<pre>', '<pre><code>')
    output = output.replace('</pre>', '</code></pre>')
    output = output.replace('<a ', '<a target=”_blank” ')
    output = output.replace('<table>', '<table border=2>')

    #ファイル生成
    output_file_path = os.path.basename(input_file_path)
    output_file_path = output_file_path.split('.')
    print(output_file_path[0])
    output_file_path = f'output/{output_file_path[0]}.html'
    with open(output_file_path, 'w') as output_file:
        output_file.write(output)
        print(f'{output_file_path} generated')




if __name__ == "__main__":
    args = sys.argv

    if args[1] == 'setup':
        setup()
    elif args[1] == 'md_to_html':
        try:
            input_file_path = args[2]
            md_to_html(input_file_path)
        except IndexError:
            print('you need to set secound arg of input file path')
