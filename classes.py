
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

        CreationPlayer.do()
        CreationEnemies.do()
        CreationCurrentItems.do()
        CreationItems.do()
        CreationEquipments.do()


class CreationPlayer:

    @classmethod
    def do(cls):
        import os.path

        check_base = os.path.exists('data')
        if not check_base:
            os.mkdir('data')

        check_file = os.path.exists('data/player.json')

        if not check_file:

            player = CreationPlayer.get()
            JsonOperations.save('player', player)

    @classmethod
    def get(cls):
        return {

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

            }

            JsonOperations.save('enemies', enemies)

    @classmethod
    def get(cls):

        return {
            'name': '',
            'equipment_id': '1',
            'location': '1',

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

                'favorite_position': '',
                'current_position': '',

                'focus': '',
                'speed': '',
                'logical': ''

            },
        }


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

                '1': CreationEquipments.get()

            }

            JsonOperations.save('equipments', equipments)

    @classmethod
    def get(cls):

        return {

                    'first_weapon': '',
                    'second_weapon': '',

                    'head': '',
                    'body': '',
                    'arms': '',
                    'legs': '',

                    'first_artifact': '',
                    'second_artifact': '',
                    'third_artifact': ''

                }


class CreationCurrentItems:

    @classmethod
    def do(cls):
        import os.path

        check_base = os.path.exists('data')
        if not check_base:
            os.mkdir('data')

        check_file = os.path.exists('data/current_items.json')

        if not check_file:
            current_items = {}

            JsonOperations.save('current_items', current_items)


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

            }

            JsonOperations.save('items', items)

    @classmethod
    def get(cls):
        return {

                    'name': '',
                    'item_type': '',

                    'slot_type': '',

                    'pierce_attack_damage': '',
                    'slash_attack_damage': '',
                    'blunt_attack_damage': '',
                    'mental_attack_damage': '',

                    'pierce_attack_resist': '',
                    'slash_attack_resist': '',
                    'blunt_attack_resist': '',
                    'mental_attack_resist': '',

                    'durability': '',
                    'weight': ''
                }


class MainMenu:

    @classmethod
    def do(cls):
        pass


class PlayerNew:

    @classmethod
    def do(cls):
        player = CreationPlayer.get()

        current_constitution = int(player['character']['constitution'])
        current_dexterity = int(player['character']['dexterity'])
        current_strength = int(player['character']['strength'])
        current_will = int(player['character']['will'])
        current_intellect = int(player['character']['current_intellect'])

        player['name'] = input('Введите имя: ')

        favorite_position = input('Какая ваша любимая позиция?')

        player['status']['favorite_position'] = favorite_position
        player['status']['current_position'] = favorite_position

        player['status']['max_health'] = str(current_constitution * 5)
        player['status']['current_health'] = str(current_constitution * 5)

        player['status']['max_stamina'] = str(current_dexterity * 3 + current_constitution + current_will)
        player['status']['current_stamina'] = str(current_dexterity * 3 + current_constitution + current_will)

        player['status']['focus'] = str(current_constitution * 3 + current_will + current_dexterity)
        player['status']['speed'] = str(current_strength * 4 + current_dexterity * 2 - current_constitution)
        player['status']['logical'] = str(current_intellect * 4 + current_will)

        JsonOperations.save('player', player)


class ItemNew:

    @classmethod
    def do(cls, item_name, item_type, slot_type, pierce_attack_damage, slash_attack_damage, blunt_attack_damage,
           mental_attack_damage, pierce_attack_resist, slash_attack_resist, blunt_attack_resist, mental_attack_resist,
           durability, weight):

        item = CreationItems.get()

        item['name'] = item_name
        item['type'] = item_type
        item['slot_type'] = slot_type
        item['pierce_attack_damage'] = pierce_attack_damage
        item['slash_attack_damage'] = slash_attack_damage
        item['blunt_attack_damage'] = blunt_attack_damage
        item['mental_attack_damage'] = mental_attack_damage
        item['pierce_attack_resist'] = pierce_attack_resist
        item['slash_attack_resist'] = slash_attack_resist
        item['blunt_attack_resist'] = blunt_attack_resist
        item['mental_attack_resist'] = mental_attack_resist
        item['durability'] = durability
        item['weight'] = weight

        items = JsonOperations.read('items')

        item_id = str(len(items) + 1)
        items[item_id] = item

        JsonOperations.save('items', items)


class ItemCurrentNew:

    @classmethod
    def do(cls, name):

        items = JsonOperations.read('items')
        current_items = JsonOperations.read('current_items')

        current_item_id = str(len(current_items) + 1)

        current_items[current_item_id] = items[name]

        JsonOperations.save('current_items', current_items)

        return current_item_id


class Maker:

    @classmethod
    def do(cls):
        pass


class ItemCreate(Maker):

    @classmethod
    def do(cls):
        #              name      type     slot   pad  sad  bad  mad  par  sar  bar  mar   dur   wgh
        # ItemNew.do('example', 'armor', 'head', '0', '0', '0', '0', '5', '5', '5', '5', '100', '3')
        ItemNew.do('Кожаный шлем', 'armor', 'head', '0', '0', '0', '0', '5', '5', '5', '5', '100', '3')
        ItemNew.do('Кожаная кираса', 'armor', 'body', '0', '0', '0', '0', '5', '5', '5', '5', '100', '3')
        ItemNew.do('Кожаные перчатки', 'armor', 'arms', '0', '0', '0', '0', '5', '5', '5', '5', '100', '3')
        ItemNew.do('Кожаные штаны', 'armor', 'legs', '0', '0', '0', '0', '5', '5', '5', '5', '100', '3')
        ItemNew.do('Простой меч', 'weapon', 'first_weapon', '12', '18', '3', '5', '0', '0', '0', '0', '100', '1')


class ItemCurrentCreateStarterPackForPlayer:

    @classmethod
    def do(cls):
        equipment = JsonOperations.read('equipment')

        equipment['1']['head'] = ItemCurrentNew.do('Кожаный шлем')
        equipment['1']['body'] = ItemCurrentNew.do('Кожаная кираса')
        equipment['1']['arms'] = ItemCurrentNew.do('Кожаные перчатки')
        equipment['1']['legs'] = ItemCurrentNew.do('Кожаные штаны')
        equipment['1']['first_weapon'] = ItemCurrentNew.do('Простой меч')

        JsonOperations.save('equipment', equipment)


class ItemCurrentCreateRandomForPlayer(Maker):

    @classmethod
    def do(cls):

        from random import choice

        items = JsonOperations.read('items')
        name = choice(list(items.keys()))

        return ItemCurrentNew.do(name)


class FightStarter:

    @classmethod
    def do(cls):
        pass


class FightRuler:

    @classmethod
    def do(cls):
        pass
