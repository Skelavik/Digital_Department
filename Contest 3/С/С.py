


def get_word():
        data = []
        with open("input.txt","r",encoding="UTF8") as file:
                line = file.read()
                data_first = (line.split("\n"))
                for couple in data_first:
                        two = couple.split()
                        data.append(two)
        return data

def math_min(data):
        min_value = 500
        for value in data:
                temporary = ''.join(value[0])
                min_value = min(min_value,int(temporary))
        return min_value

data = get_word()

while True:

        timer = 480
        count_sessions, count_sosich = data[0][0],data[0][1]
        data.remove(data[0])
        print(count_sessions,count_sosich)
        print(data)


        break