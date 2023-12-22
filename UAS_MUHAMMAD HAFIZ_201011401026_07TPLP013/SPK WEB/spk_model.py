from settings import DEV_SCALE_model,DEV_SCALE_ram,DEV_SCALE_processor,DEV_SCALE_storage,DEV_SCALE_battery_capacity,DEV_SCALE_price,DEV_SCALE_screen_size

class BaseMethod():

    def __init__(self, data_dict, **setWeight):

        self.dataDict = data_dict

        # 1-7 (Kriteria)
        self.raw_weight = {
            'model': 5, 
            'ram': 3, 
            'processor': 4, 
            'storage': 3, 
            'battery_capacity': 4, 
            'screen_size': 3, 
            'price': 1
        }

        if setWeight:
            for item in setWeight.items():
                temp1 = setWeight[item[0]] # value int
                temp2 = {v: k for k, v in setWeight.items()}[item[1]] # key str

                setWeight[item[0]] = item[1]
                setWeight[temp2] = temp1

    @property
    def weight(self):
        total_weight = sum(self.raw_weight.values())
        return {c: round(w/total_weight, 2) for c,w in self.raw_weight.items()}

    @property
    def data(self):
        return [{
            'id': smartphone['id'],
            'model': DEV_SCALE_model[smartphone['model']],
            'ram': DEV_SCALE_ram[smartphone['ram']],
            'processor': DEV_SCALE_processor[smartphone['processor']],
            'storage': DEV_SCALE_storage[smartphone['storage']],
            'battery_capacity': DEV_SCALE_battery_capacity[smartphone['battery_capacity']],
            'screen_size': DEV_SCALE_screen_size[smartphone['screen_size']],
            'price': DEV_SCALE_price[smartphone['price']]
        } for smartphone in self.dataDict]

    @property
    def normalized_data(self):
        # x/max [benefit]
        # min/x [cost]
        model = [] # max
        ram = [] # max
        processor = [] # max
        storage = [] # max
        battery_capacity = [] # max
        screen_size = [] # max
        price = [] # min
        for data in self.data:
            model.append(data['model'])
            ram.append(data['ram'])
            processor.append(data['processor'])
            storage.append(data['storage'])
            battery_capacity.append(data['battery_capacity'])
            screen_size.append(data['screen_size'])
            price.append(data['price'])

        max_model = max(model)
        max_ram = max(ram)
        max_processor = max(processor)
        max_storage = max(storage)
        max_battery_capacity = max(battery_capacity)
        max_screen_size = max(screen_size)
        min_price = min(price)

        return [
            {   'id': data['id'],
                'model': data['model']/max_model, # benefit
                'ram': data['ram']/max_ram, # benefit
                'processor': data['processor']/max_processor, # benefit
                'storage': data['storage']/max_storage, # benefit
                'battery_capacity': data['battery_capacity']/max_battery_capacity, # benefit
                'screen_size': data['screen_size']/max_screen_size, # benefit
                'price': min_price/data['price'] # cost
                }
            for data in self.data
        ]
 

class WeightedProduct(BaseMethod):
    def __init__(self, dataDict, setWeight:dict):
        super().__init__(data_dict=dataDict, **setWeight)
    @property
    def calculate(self):
        weight = self.weight
        result = {row['id']:
    round(
        row['model'] ** weight['model'] *
        row['ram'] ** weight['ram'] *
        row['processor'] ** weight['processor'] *
        row['storage'] ** weight['storage'] *
        row['battery_capacity'] ** weight['battery_capacity'] *
        row['screen_size'] ** (-weight['screen_size']) *
        row['price'] ** weight['price']
        , 2
    )
    for row in self.normalized_data}

        #sorting
        # return result
        return dict(sorted(result.items(), key=lambda x:x[1], reverse=True))