
class JsonOperations:

    @classmethod
    def read(cls, ref):
        """Импортирует JSON в Python, и возвращает его значение.
        Аргументы: ref - ссылка на JSON, который надо присвоить переменной."""
        from json import load
        with open('data/' + ref + '.json') as json_import_data:
            data_file = load(json_import_data)
        return data_file

    @classmethod
    def save(cls, ref, data_file):
        """Сохраняет значение переменной в JSON.
        Аргументы: ref - ссылка на JSON, data_file - переменная,
        значение которой сохраняется в JSON."""
        from json import dump
        with open('data/' + ref + '.json', 'w') as add_info_file:
            dump(data_file, add_info_file)


class Initialization:

    @classmethod
    def do(cls):
        pass


class CreationPlayer:

    @classmethod
    def do(cls):
        import os.path

        check_base = os.path.exists('data')
        if not check_base:
            os.mkdir('data')

        check_file = os.path.exists('data/player.json')

        if not check_file:

            player = {

                'name': '',

                'location': '',

                'character': {

                    'strength': '5',
                    'dexterity': '5',
                    'intellect': '5',
                    'constitution': '5',
                    'will': '5',

                },


                'skills': {

                    'swords': '0',
                    'axes': '0',
                    'spears': '0',
                    'hummers': '0',

                },

                'status': {

                    'max_health': '',
                    'current_health': '',

                    'max_stamina': '',
                    'current_stamina': '',

                    'focus': '',
                    'speed': '',

                    'alive': 'False'
                },
            }

            JsonOperations.save('database', player)


class CreationEnemies:

    @classmethod
    def do(cls):
        import os.path

        check_base = os.path.exists('data')
        if not check_base:
            os.mkdir('data')

        check_file = os.path.exists('data/enemies.json')

        if not check_file:
            enemies = {

                '0': {
                    'name': '',
                    'equipment_id': '',
                    'location': '',

                    'character': {

                         'strength': '5',
                         'dexterity': '5',
                         'intellect': '5',
                         'constitution': '5',
                         'will': '5',

                     },

                    'skills': {

                         'swords': '0',
                         'axes': '0',
                         'spears': '0',
                         'hummers': '0',

                     },

                    'status': {

                         'max_health': '',
                         'current_health': '',

                         'max_stamina': '',
                         'current_stamina': '',

                         'focus': '',
                         'speed': '',

                     },
                 },
            }

            JsonOperations.save('database', enemies)


class CreationEquipments:

    @classmethod
    def do(cls):
        import os.path

        check_base = os.path.exists('data')
        if not check_base:
            os.mkdir('data')

        check_file = os.path.exists('data/equipments.json')

        if not check_file:
            equipments = {
                'equipment_id': {

                    'head': '',
                    'body': '',
                    'arms': '',
                    'legs': ''

                },
            }

            JsonOperations.save('database', equipments)


class CreationItems:

    @classmethod
    def do(cls):
        import os.path

        check_base = os.path.exists('data')
        if not check_base:
            os.mkdir('data')

        check_file = os.path.exists('data/items.json')

        if not check_file:
            items = {
                'equipment_id': {

                    'first_weapon': '',
                    'second_weapon': '',

                    'head': '',
                    'body': '',
                    'arms': '',
                    'legs': ''

                },
            }

            JsonOperations.save('database', items)


class MainMenu:

    @classmethod
    def do(cls):
        pass


class CreationCharacter:

    @classmethod
    def do(cls):
        pass


class FightStarter:

    @classmethod
    def do(cls):
        pass


class FightRuler:

    @classmethod
    def do(cls):
        pass
