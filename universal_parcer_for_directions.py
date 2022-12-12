import requests
from bs4 import BeautifulSoup as BS


class Parse:
    def __init__(self, url):
        self.url = url
        self.hse_directions = requests.get(f'{url}admission')
        self.header = requests.get(f'{url}')
        self.message = str()
        self.all_descriptions_with_info = {}

    def parcing(self):
        soup = BS(self.hse_directions.content, 'lxml')
        description = soup.find_all(class_="b-program__property-title")
        description_info = soup.find_all(class_="b-program__property-value")
        temp_1_desc = {}
        temp_2_info = {}
        if self.url == "https://www.hse.ru/ba/transport/":
            soup = BS(self.header.content, 'lxml')
            big_header = soup.find(class_="header-content").find("h1", class_="first_child")
            header = soup.find(class_="header-content").find("p", class_="first_child last_child")
            print(big_header)
            print(header)
            header_descr = str()
            message_end = str()
            header_header = str()
            message_addittion = str()
            for iterororo_2 in big_header:
                header_header += iterororo_2.text
            for iterororo in header:
                header_descr += iterororo.text
            message_addittion = f'{header_header}\n\n{header_descr}\n\n'
            print(message_addittion)
            print(message_end)
            self.message = message_addittion + message_end
        else:
            if self.url == "https://www.hse.ru/ba/compsocsci/":
                count = 6
            else:
                count = 7
            message_end = str()
            i = 1
            j = 1
            for iter in description:
                temp_1_desc[i] = iter.text
                i += 1
            for iter_2 in description_info:
                temp_2_info[j] = iter_2.text
                j += 1
            iterator = 1
            for iterator in range(1, count):
                message_end += f'{temp_1_desc[iterator]}:\n{temp_2_info[iterator]}\n\n'
            soup = BS(self.header.content, 'lxml')
            big_header = soup.find(class_="header-content").find(class_="first_child")
            header = soup.find(class_="header-content").find(class_="first_child last_child")
            first_header = soup.find(class_="header-content").find("p", class_="first_child")
            second_header = soup.find(class_="header-content").find(class_="last_child")

            if header:
                header_descr = str()
                header_header = str()
                message_addittion = str()
                for iterororo_2 in big_header:
                    header_header += iterororo_2.text
                for iterororo in header:
                    header_descr += iterororo.text
                message_addittion = f'{header_header}\n\n{header_descr}\n\n'
                print(message_addittion)
                print(message_end)
                self.message = message_addittion + message_end

            elif (first_header and second_header):
                header_descr = str()
                header_header = str()
                message_addittion = str()
                for iterororo_2 in big_header:
                    header_header += iterororo_2.text
                for iteror_1 in first_header:
                    header_descr += iteror_1.text
                for iteror_2 in second_header:
                    header_descr += iteror_2.text
                message_addittion = f'{header_header}\n\n{header_descr}\n\n'
                print(message_addittion)
                print(message_end)
                self.message = message_addittion + message_end

            else:
                new_type_header = soup.find(class_="g larger").find(class_="first_child")
                header_descr = str()
                message_addittion = str()
                for iteror_1 in new_type_header:
                    header_descr += iteror_1.text
                message_addittion = f'{header_descr}\n\n'
                print(message_addittion)
                print(message_end)
                self.message = message_addittion + message_end
        self.message += f'\nЧтобы ознакомиться с подробной информацией, переходи по ссылке: {self.url}'
        return self.message
