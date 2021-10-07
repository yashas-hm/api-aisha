from Constants import *
import string


class Splitter:
    def __init__(self, data):
        self.data = str(data).strip()
        self.render = {
            'intent': '',
            'specification': '',
            'task': '',
            'talk back': ''
        }

    def start_split(self):
        self.remove_wake_word()
        self.check_render()
        return self.render

    def remove_wake_word(self):
        wake = str(self.data).lower().split(' ')
        joint = ' '

        remove = []
        for i in range(len(wake)):
            if wake[i] in Constants.GREET_WORDS:
                remove.append(wake[i])
            if wake[i] in Constants.AISHA:
                remove.append(wake[i])

        for i in remove:
            wake.remove(i)

        self.data = joint.join(wake)

    def check_render(self):
        joint = ' '
        render = str(self.data).lower().split(' ')
        length = len(render)

        if render[length - 1] == 'music':
            if render[length - 2] in Constants.SPECIFIC_PLATFORM:
                self.render['specification'] = joint.join([render[length - 2], render[length - 1]])
                render.remove(render[length - 1])
                render.remove(render[length - 2])
                if render[length - 3] == 'in' or render[length - 3] == 'on':
                    render.remove(render[length - 3])

        elif render[length - 1] == 'prime':
            if render[length - 2] in Constants.SPECIFIC_PLATFORM:
                self.render['specification'] = joint.join([render[length - 2], render[length - 1]])
                render.remove(render[length - 1])
                render.remove(render[length - 2])
                if render[length - 3] == 'in' or render[length - 3] == 'on':
                    render.remove(render[length - 3])

        elif render[length - 1] in Constants.SPECIFIC_PLATFORM:
            self.render['specification'] = render[length - 1]
            render.remove(render[length - 1])
            if render[length - 2] == 'in' or render[length - 2] == 'on':
                render.remove(render[length - 2])

        if render[0] in Constants.CONTROL:

            if render[0] == 'turn' or render[0] == 'switch':
                self.render['intent'] = joint.join([render[0], render[1]])
                render.remove(render[0])
                render.remove(render[0])
            else:
                self.render['intent'] = render[0]
                render.remove(render[0])

            self.render['task'] = joint.join(render)
        print(render)
        print(self.data)
        data = str(self.data).translate(str.maketrans('', '', string.punctuation))
        if data in Constants.GENERAL_STATEMENTS.keys():
            self.render['intent'] = 'talk'
            self.render['talk back'] = Constants.GENERAL_STATEMENTS[data]

        if self.render['intent'] != '' and self.render['intent'] != 'talk':
            self.render['talk back'] = 'Getting that in a minute!'
        elif self.render['intent'] != 'talk':
            self.render['talk back'] = 'Sorry I could not understand that.'


# if __name__ == '__main__':
#     d = ''
#     while d != 'ee':
#         d = str(input('Me: '))
#         print('A.I.S.H.A: ', Splitter(d).start_split())
