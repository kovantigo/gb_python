from re import search

with open('nginx_logs.txt', 'r', encoding='utf-8') as r_file:
    logs = (item for item in r_file)
    my_gen = ((search(r"(([\d]+\.){3}[\d]+)|(([a-z0-9]+[:]|[::]){4,8}[a-z0-9]+)", log)[0], # IPv4 and IPv6
                search(r"\[[\w/:+\s]+\]", log)[0].replace('[', '').replace(']', ''), # Date/Time
                search(r"\"[A-Z]{3,4}", log)[0].replace('"', ''), # type request
                search(r"(/[a-z0-9_]+){2}", log)[0], # requested resource
                *search(r"(\s[\d]+){2}", log)[0].replace(' ', '', 1).rsplit(' ', maxsplit=1)) # response code, size
                for log in logs)
    with open('logs.txt', 'w', encoding='utf-8') as w_file:
        for log in my_gen:
            w_file.write(f'{log}\n')
