import sys
import csv

class Args(object):
    def __init__(self):
        self.args = sys.argv[1:]

    def get_arg(self, arg):
        try:
            file_path = self.args[self.args.index(arg) + 1]
            return file_path
        except:
            print('ERROR')

class Config(object):
    def __init__(self, file_path):
        self._config = self._read_config(file_path)
    def _read_config(self, file_path):
        config = {}
        with open(file_path, 'r') as f:
            for line in f:
                key,  value = line.split('=')
                key = key.strip()
                try:
                    value = float(value.strip())
                except ValueError:
                    continue
                config[key] = value
            return config
    def get_config(self, key):
        return self._config[key]
    def total_rate(self):
        rates = self._config[YangLao] + self._config[YiLiao] + self._config[ShiYe] + self._config[GongJiJin] + self._config[GongShang] + self._config[ShengYu]
        return rates

class UserData(object):
    def __init__(self, file_path):
        self._userdata = self._read_users_data(file_path)
    def _read_users_data(self, file_path):
        userdata = {}
        with open(file_path, 'r') as f:
            for line in f:
                emploee_id, gongzi = line.split(',')
                userdata[int(emploee_id)] = int(gongzi)
            return userdata
    def get_userdata(self, emploee_id):
        return self._userdata[emploee_id]

class IncomeTaxCalculator(object):
    def __init__(self, userdata, configfile):
        self.shuju = self._calculator(userdata, configfile)
    def _calculator(self, userdata, configfile):
        shuju = []
        for key, value in userdata.items():
            if value < configfile.get_config('JiShuL'):
                shebao = round(configfile.get_config('JiShuL') * 0.165, 2)
            elif value > configfile.get_config('JiShuH'):
                shebao = round(configfile.get_config('JiShuH') * 0.165, 2)
            else:
                shebao = round(value * 0.165, 2)
            left_gongzi = value - shebao
            tax_left_gongzi =  left_gongzi - 3500
            if tax_left_gongzi > 0 and tax_left_gongzi < 1500:
                tax = round(tax_left_gongzi * 0.03 - 0, 2)
            elif tax_left_gongzi >= 1500 and tax_left_gongzi < 4500:
                tax = round(tax_left_gongzi * 0.1 - 105, 2)
            elif tax_left_gongzi >= 4500 and tax_left_gongzi < 9000:
                tax = round(tax_left_gongzi * 0.2 - 555, 2)
            elif tax_left_gongzi >= 9000 and tax_left_gongzi < 35000:
                tax = round(tax_left_gongzi * 0.25 - 1005, 2)
            elif tax_left_gongzi >= 35000 and tax_left_gongzi < 55000:
                tax = round(tax_left_gongzi * 0.3 - 2755, 2)
            elif tax_left_gongzi >= 55000 and tax_left_gongzi < 80000:
                tax = round(tax_left_gongzi * 0.35 - 5505, 2)
            elif tax_left_gongzi >= 80000:
                tax = round(tax_left_gongzi * 0.45 - 13505, 2)
            else:
                tax = 0.00
            last_gongzi = left_gongzi - tax
            #print(key, value, shebao, tax, last_gongzi)
            shuju.append([str(key), str(value), str(shebao), str(tax), str(last_gongzi)])
        return shuju

class ExportData(object):
    def __init__(self, shuju):
        self.shuju = shuju
    def exports(self, file_path):
        with open(file_path, 'w') as f:
            for i in self.shuju:
                line = ','.join(i)
                f.write(line)
                f.write('\n')

conf_file = Args()
configtest = Config(conf_file.get_arg('-c'))
userdatatest = UserData(conf_file.get_arg('-d'))
incometaxc = IncomeTaxCalculator(userdatatest._userdata, configtest)
exportok = ExportData(incometaxc.shuju)
exportok.exports(conf_file.get_arg('-o'))

