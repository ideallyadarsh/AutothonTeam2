import string
import sys
import os
sys.path.insert(0, os.path.dirname(os.getcwd()))
from faker import Faker
import random
import re
import datetime
import pytz
# from email_validator import validate_email, EmailNotValidError

# initialize Faker
from Shell_FE_Selenium_Core.Utilities.LoggingUtilities import LoggingUtilities

fake = Faker()


class RandomTestDataGenerator:

    """"
   This random test generator class will provide multiple methods to generate a random data like
   First_Name, Last_Name, full_name, ID, Address, Phone_Number, Email etc
    """
    try:

        logobj = LoggingUtilities()
        log = logobj.logger()
    except Exception:
        raise "File error"

    @staticmethod
    def get_name(name_type):

        """
        This method will generate and return First_Name, Last_Name and full_name
        :param name_type: name_type format first_name, last_name , full_name
        """
        if name_type == "full_name":
            name = fake.name()
            RandomTestDataGenerator.log.info(f"Random test data utility generated Full name is : {name}")
        elif name_type == "first_name":
            name = fake.first_name()
            RandomTestDataGenerator.log.info(f"Random test data utility generated First name is : {name}")
        elif name_type == "last_name":
            name = fake.last_name()
            RandomTestDataGenerator.log.info(f"Random test data utility generated last name is : {name}")
        else:
            RandomTestDataGenerator.log.error("Invalid name format provide to generate random data")
            raise Exception("Invalid name format, name format should be first_name, last_name or full_name")

        return name

    @staticmethod
    def get_address(localization="en_US"):
        """"
        Random address method will return the address.
        :param localization: User can pass the localization as param , default its set to "en_US"
        """
        try:
            f = Faker(locale=localization)
            address = f.address()
            RandomTestDataGenerator.log.info(f"Random test data utility generated address is : {address}")

        except Exception:
            raise "Invalid localization, please provide valid localization ex: en_US, en_IN, en_CA etc"
        return address

    @staticmethod
    def get_date_time(date_time, date_pattern= '%d-%m-%Y', time_pattern='%H:%M:%S'):
        """
           This method will generate and return date , time or date time both
           :param date_time: date_time values are date, time, datetime
           :param date_pattern: Takes the date pattern
           :param time_pattern: time pattern
           """
        if date_time == 'time':
            date_time_value = fake.time(pattern=time_pattern)
            RandomTestDataGenerator.log.info(f"Random test data utility generated : {date_time_value}")
        elif date_time == 'date':
            date_time_value = fake.date(pattern=date_pattern)
            RandomTestDataGenerator.log.info(f"Random test data utility generated date : {date_time_value}")
        elif date_time == 'datetime':
            date_time_value = fake.date_time()
            RandomTestDataGenerator.log.info(f"Random test data utility generated Date and Time : {date_time_value}")
        else:
            RandomTestDataGenerator.log.error("Invalid date time format provided to random test data utility")
            raise Exception("Invalid date or time type , date_time format ex: time, date or datetime")
        return date_time_value

    @staticmethod
    def get_current_datetime(time_zone='Australia\Victoria'):
        """
        This method will return the current date and time based on time zone provided.
        :param timezone : Time zone info
        Time Zone Ex: ['Africa/Abidjan', 'Africa/Accra', 'Africa/Addis_Ababa', 'Africa/Algiers', 'Africa/Asmara', 'Africa/Asmera', 'Africa/Bamako', 'Africa/Bangui', 'Africa/Banjul', 'Africa/Bissau', 'Africa/Blantyre', 'Africa/Brazzaville', 'Africa/Bujumbura', 'Africa/Cairo', 'Africa/Casablanca', 'Africa/Ceuta', 'Africa/Conakry', 'Africa/Dakar', 'Africa/Dar_es_Salaam', 'Africa/Djibouti', 'Africa/Douala', 'Africa/El_Aaiun', 'Africa/Freetown', 'Africa/Gaborone', 'Africa/Harare', 'Africa/Johannesburg', 'Africa/Juba', 'Africa/Kampala', 'Africa/Khartoum', 'Africa/Kigali', 'Africa/Kinshasa', 'Africa/Lagos', 'Africa/Libreville', 'Africa/Lome', 'Africa/Luanda', 'Africa/Lubumbashi', 'Africa/Lusaka', 'Africa/Malabo', 'Africa/Maputo', 'Africa/Maseru', 'Africa/Mbabane', 'Africa/Mogadishu', 'Africa/Monrovia', 'Africa/Nairobi', 'Africa/Ndjamena', 'Africa/Niamey', 'Africa/Nouakchott', 'Africa/Ouagadougou', 'Africa/Porto-Novo', 'Africa/Sao_Tome', 'Africa/Timbuktu', 'Africa/Tripoli', 'Africa/Tunis', 'Africa/Windhoek', 'America/Adak', 'America/Anchorage', 'America/Anguilla', 'America/Antigua', 'America/Araguaina', 'America/Argentina/Buenos_Aires', 'America/Argentina/Catamarca', 'America/Argentina/ComodRivadavia', 'America/Argentina/Cordoba', 'America/Argentina/Jujuy', 'America/Argentina/La_Rioja', 'America/Argentina/Mendoza', 'America/Argentina/Rio_Gallegos', 'America/Argentina/Salta', 'America/Argentina/San_Juan', 'America/Argentina/San_Luis', 'America/Argentina/Tucuman', 'America/Argentina/Ushuaia', 'America/Aruba', 'America/Asuncion', 'America/Atikokan', 'America/Atka', 'America/Bahia', 'America/Bahia_Banderas', 'America/Barbados', 'America/Belem', 'America/Belize', 'America/Blanc-Sablon', 'America/Boa_Vista', 'America/Bogota', 'America/Boise', 'America/Buenos_Aires', 'America/Cambridge_Bay', 'America/Campo_Grande', 'America/Cancun', 'America/Caracas', 'America/Catamarca', 'America/Cayenne', 'America/Cayman', 'America/Chicago', 'America/Chihuahua', 'America/Coral_Harbour', 'America/Cordoba', 'America/Costa_Rica', 'America/Creston', 'America/Cuiaba', 'America/Curacao', 'America/Danmarkshavn', 'America/Dawson', 'America/Dawson_Creek', 'America/Denver', 'America/Detroit', 'America/Dominica', 'America/Edmonton', 'America/Eirunepe', 'America/El_Salvador', 'America/Ensenada', 'America/Fort_Nelson', 'America/Fort_Wayne', 'America/Fortaleza', 'America/Glace_Bay', 'America/Godthab', 'America/Goose_Bay', 'America/Grand_Turk', 'America/Grenada', 'America/Guadeloupe', 'America/Guatemala', 'America/Guayaquil', 'America/Guyana', 'America/Halifax', 'America/Havana', 'America/Hermosillo', 'America/Indiana/Indianapolis', 'America/Indiana/Knox', 'America/Indiana/Marengo', 'America/Indiana/Petersburg', 'America/Indiana/Tell_City', 'America/Indiana/Vevay', 'America/Indiana/Vincennes', 'America/Indiana/Winamac', 'America/Indianapolis', 'America/Inuvik', 'America/Iqaluit', 'America/Jamaica', 'America/Jujuy', 'America/Juneau', 'America/Kentucky/Louisville', 'America/Kentucky/Monticello', 'America/Knox_IN', 'America/Kralendijk', 'America/La_Paz', 'America/Lima', 'America/Los_Angeles', 'America/Louisville', 'America/Lower_Princes', 'America/Maceio', 'America/Managua', 'America/Manaus', 'America/Marigot', 'America/Martinique', 'America/Matamoros', 'America/Mazatlan', 'America/Mendoza', 'America/Menominee', 'America/Merida', 'America/Metlakatla', 'America/Mexico_City', 'America/Miquelon', 'America/Moncton', 'America/Monterrey', 'America/Montevideo', 'America/Montreal', 'America/Montserrat', 'America/Nassau', 'America/New_York', 'America/Nipigon', 'America/Nome', 'America/Noronha', 'America/North_Dakota/Beulah', 'America/North_Dakota/Center', 'America/North_Dakota/New_Salem', 'America/Nuuk', 'America/Ojinaga', 'America/Panama', 'America/Pangnirtung', 'America/Paramaribo', 'America/Phoenix', 'America/Port-au-Prince', 'America/Port_of_Spain', 'America/Porto_Acre', 'America/Porto_Velho', 'America/Puerto_Rico', 'America/Punta_Arenas', 'America/Rainy_River', 'America/Rankin_Inlet', 'America/Recife', 'America/Regina', 'America/Resolute', 'America/Rio_Branco', 'America/Rosario', 'America/Santa_Isabel', 'America/Santarem', 'America/Santiago', 'America/Santo_Domingo', 'America/Sao_Paulo', 'America/Scoresbysund', 'America/Shiprock', 'America/Sitka', 'America/St_Barthelemy', 'America/St_Johns', 'America/St_Kitts', 'America/St_Lucia', 'America/St_Thomas', 'America/St_Vincent', 'America/Swift_Current', 'America/Tegucigalpa', 'America/Thule', 'America/Thunder_Bay', 'America/Tijuana', 'America/Toronto', 'America/Tortola', 'America/Vancouver', 'America/Virgin', 'America/Whitehorse', 'America/Winnipeg', 'America/Yakutat', 'America/Yellowknife', 'Antarctica/Casey', 'Antarctica/Davis', 'Antarctica/DumontDUrville', 'Antarctica/Macquarie', 'Antarctica/Mawson', 'Antarctica/McMurdo', 'Antarctica/Palmer', 'Antarctica/Rothera', 'Antarctica/South_Pole', 'Antarctica/Syowa', 'Antarctica/Troll', 'Antarctica/Vostok', 'Arctic/Longyearbyen', 'Asia/Aden', 'Asia/Almaty', 'Asia/Amman', 'Asia/Anadyr', 'Asia/Aqtau', 'Asia/Aqtobe', 'Asia/Ashgabat', 'Asia/Ashkhabad', 'Asia/Atyrau', 'Asia/Baghdad', 'Asia/Bahrain', 'Asia/Baku', 'Asia/Bangkok', 'Asia/Barnaul', 'Asia/Beirut', 'Asia/Bishkek', 'Asia/Brunei', 'Asia/Calcutta', 'Asia/Chita', 'Asia/Choibalsan', 'Asia/Chongqing', 'Asia/Chungking', 'Asia/Colombo', 'Asia/Dacca', 'Asia/Damascus', 'Asia/Dhaka', 'Asia/Dili', 'Asia/Dubai', 'Asia/Dushanbe', 'Asia/Famagusta', 'Asia/Gaza', 'Asia/Harbin', 'Asia/Hebron', 'Asia/Ho_Chi_Minh', 'Asia/Hong_Kong', 'Asia/Hovd', 'Asia/Irkutsk', 'Asia/Istanbul', 'Asia/Jakarta', 'Asia/Jayapura', 'Asia/Jerusalem', 'Asia/Kabul', 'Asia/Kamchatka', 'Asia/Karachi', 'Asia/Kashgar', 'Asia/Kathmandu', 'Asia/Katmandu', 'Asia/Khandyga', 'Asia/Kolkata', 'Asia/Krasnoyarsk', 'Asia/Kuala_Lumpur', 'Asia/Kuching', 'Asia/Kuwait', 'Asia/Macao', 'Asia/Macau', 'Asia/Magadan', 'Asia/Makassar', 'Asia/Manila', 'Asia/Muscat', 'Asia/Nicosia', 'Asia/Novokuznetsk', 'Asia/Novosibirsk', 'Asia/Omsk', 'Asia/Oral', 'Asia/Phnom_Penh', 'Asia/Pontianak', 'Asia/Pyongyang', 'Asia/Qatar', 'Asia/Qostanay', 'Asia/Qyzylorda', 'Asia/Rangoon', 'Asia/Riyadh', 'Asia/Saigon', 'Asia/Sakhalin', 'Asia/Samarkand', 'Asia/Seoul', 'Asia/Shanghai', 'Asia/Singapore', 'Asia/Srednekolymsk', 'Asia/Taipei', 'Asia/Tashkent', 'Asia/Tbilisi', 'Asia/Tehran', 'Asia/Tel_Aviv', 'Asia/Thimbu', 'Asia/Thimphu', 'Asia/Tokyo', 'Asia/Tomsk', 'Asia/Ujung_Pandang', 'Asia/Ulaanbaatar', 'Asia/Ulan_Bator', 'Asia/Urumqi', 'Asia/Ust-Nera', 'Asia/Vientiane', 'Asia/Vladivostok', 'Asia/Yakutsk', 'Asia/Yangon', 'Asia/Yekaterinburg', 'Asia/Yerevan', 'Atlantic/Azores', 'Atlantic/Bermuda', 'Atlantic/Canary', 'Atlantic/Cape_Verde', 'Atlantic/Faeroe', 'Atlantic/Faroe', 'Atlantic/Jan_Mayen', 'Atlantic/Madeira', 'Atlantic/Reykjavik', 'Atlantic/South_Georgia', 'Atlantic/St_Helena', 'Atlantic/Stanley', 'Australia/ACT', 'Australia/Adelaide', 'Australia/Brisbane', 'Australia/Broken_Hill', 'Australia/Canberra', 'Australia/Currie', 'Australia/Darwin', 'Australia/Eucla', 'Australia/Hobart', 'Australia/LHI', 'Australia/Lindeman', 'Australia/Lord_Howe', 'Australia/Melbourne', 'Australia/NSW', 'Australia/North', 'Australia/Perth', 'Australia/Queensland', 'Australia/South', 'Australia/Sydney', 'Australia/Tasmania', 'Australia/Victoria', 'Australia/West', 'Australia/Yancowinna', 'Brazil/Acre', 'Brazil/DeNoronha', 'Brazil/East', 'Brazil/West', 'CET', 'CST6CDT', 'Canada/Atlantic', 'Canada/Central', 'Canada/Eastern', 'Canada/Mountain', 'Canada/Newfoundland', 'Canada/Pacific', 'Canada/Saskatchewan', 'Canada/Yukon', 'Chile/Continental', 'Chile/EasterIsland', 'Cuba', 'EET', 'EST', 'EST5EDT', 'Egypt', 'Eire', 'Etc/GMT', 'Etc/GMT+0', 'Etc/GMT+1', 'Etc/GMT+10', 'Etc/GMT+11', 'Etc/GMT+12', 'Etc/GMT+2', 'Etc/GMT+3', 'Etc/GMT+4', 'Etc/GMT+5', 'Etc/GMT+6', 'Etc/GMT+7', 'Etc/GMT+8', 'Etc/GMT+9', 'Etc/GMT-0', 'Etc/GMT-1', 'Etc/GMT-10', 'Etc/GMT-11', 'Etc/GMT-12', 'Etc/GMT-13', 'Etc/GMT-14', 'Etc/GMT-2', 'Etc/GMT-3', 'Etc/GMT-4', 'Etc/GMT-5', 'Etc/GMT-6', 'Etc/GMT-7', 'Etc/GMT-8', 'Etc/GMT-9', 'Etc/GMT0', 'Etc/Greenwich', 'Etc/UCT', 'Etc/UTC', 'Etc/Universal', 'Etc/Zulu', 'Europe/Amsterdam', 'Europe/Andorra', 'Europe/Astrakhan', 'Europe/Athens', 'Europe/Belfast', 'Europe/Belgrade', 'Europe/Berlin', 'Europe/Bratislava', 'Europe/Brussels', 'Europe/Bucharest', 'Europe/Budapest', 'Europe/Busingen', 'Europe/Chisinau', 'Europe/Copenhagen', 'Europe/Dublin', 'Europe/Gibraltar', 'Europe/Guernsey', 'Europe/Helsinki', 'Europe/Isle_of_Man', 'Europe/Istanbul', 'Europe/Jersey', 'Europe/Kaliningrad', 'Europe/Kiev', 'Europe/Kirov', 'Europe/Lisbon', 'Europe/Ljubljana', 'Europe/London', 'Europe/Luxembourg', 'Europe/Madrid', 'Europe/Malta', 'Europe/Mariehamn', 'Europe/Minsk', 'Europe/Monaco', 'Europe/Moscow', 'Europe/Nicosia', 'Europe/Oslo', 'Europe/Paris', 'Europe/Podgorica', 'Europe/Prague', 'Europe/Riga', 'Europe/Rome', 'Europe/Samara', 'Europe/San_Marino', 'Europe/Sarajevo', 'Europe/Saratov', 'Europe/Simferopol', 'Europe/Skopje', 'Europe/Sofia', 'Europe/Stockholm', 'Europe/Tallinn', 'Europe/Tirane', 'Europe/Tiraspol', 'Europe/Ulyanovsk', 'Europe/Uzhgorod', 'Europe/Vaduz', 'Europe/Vatican', 'Europe/Vienna', 'Europe/Vilnius', 'Europe/Volgograd', 'Europe/Warsaw', 'Europe/Zagreb', 'Europe/Zaporozhye', 'Europe/Zurich', 'GB', 'GB-Eire', 'GMT', 'GMT+0', 'GMT-0', 'GMT0', 'Greenwich', 'HST', 'Hongkong', 'Iceland', 'Indian/Antananarivo', 'Indian/Chagos', 'Indian/Christmas', 'Indian/Cocos', 'Indian/Comoro', 'Indian/Kerguelen', 'Indian/Mahe', 'Indian/Maldives', 'Indian/Mauritius', 'Indian/Mayotte', 'Indian/Reunion', 'Iran', 'Israel', 'Jamaica', 'Japan', 'Kwajalein', 'Libya', 'MET', 'MST', 'MST7MDT', 'Mexico/BajaNorte', 'Mexico/BajaSur', 'Mexico/General', 'NZ', 'NZ-CHAT', 'Navajo', 'PRC', 'PST8PDT', 'Pacific/Apia', 'Pacific/Auckland', 'Pacific/Bougainville', 'Pacific/Chatham', 'Pacific/Chuuk', 'Pacific/Easter', 'Pacific/Efate', 'Pacific/Enderbury', 'Pacific/Fakaofo', 'Pacific/Fiji', 'Pacific/Funafuti', 'Pacific/Galapagos', 'Pacific/Gambier', 'Pacific/Guadalcanal', 'Pacific/Guam', 'Pacific/Honolulu', 'Pacific/Johnston', 'Pacific/Kanton', 'Pacific/Kiritimati', 'Pacific/Kosrae', 'Pacific/Kwajalein', 'Pacific/Majuro', 'Pacific/Marquesas', 'Pacific/Midway', 'Pacific/Nauru', 'Pacific/Niue', 'Pacific/Norfolk', 'Pacific/Noumea', 'Pacific/Pago_Pago', 'Pacific/Palau', 'Pacific/Pitcairn', 'Pacific/Pohnpei', 'Pacific/Ponape', 'Pacific/Port_Moresby', 'Pacific/Rarotonga', 'Pacific/Saipan', 'Pacific/Samoa', 'Pacific/Tahiti', 'Pacific/Tarawa', 'Pacific/Tongatapu', 'Pacific/Truk', 'Pacific/Wake', 'Pacific/Wallis', 'Pacific/Yap', 'Poland', 'Portugal', 'ROC', 'ROK', 'Singapore', 'Turkey', 'UCT', 'US/Alaska', 'US/Aleutian', 'US/Arizona', 'US/Central', 'US/East-Indiana', 'US/Eastern', 'US/Hawaii', 'US/Indiana-Starke', 'US/Michigan', 'US/Mountain', 'US/Pacific', 'US/Samoa', 'UTC', 'Universal', 'W-SU', 'WET', 'Zulu']
        """
        try:
            date_time = datetime.datetime.now(pytz.timezone(time_zone))
            RandomTestDataGenerator.log.info(f"Current Date & Time is: {date_time} and time zone is : {time_zone}")

        except Exception:
            raise "Invalid time zone provided, please provide valid time zone"
        # return date_time


    @staticmethod
    def get_email(domain, length=8):

        """
           This method will generate a alpha numeric email ID and adds the user provided domain name
           :param domain: domain examples Shell.com, gmail.com, test.co.in etc
           """

        # email_pattern = '^[a-zA-Z0-9_.]+@\w+(\.[a-z]{2,3})(\.[a-z]{2,3})'

        email_pattern = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+(\.[a-z]{2,3})+'
        email = RandomTestDataGenerator.random_char(length) + "@" + domain
        if re.fullmatch(email_pattern, email):
            RandomTestDataGenerator.log.info(f"Random test data utility generated Email : {email}")
            return email
        else:
            RandomTestDataGenerator.log.error("Invalid domain name provided to generate random email")
            raise Exception("Invalid email domain format, Email domain format ex: Shell.com, test.co.in, .org etc")
        # try:
        #     valid = validate_email(email)
        #     print(email)
        # except EmailNotValidError as e:
        #     print(str(e))

    @staticmethod
    def get_phone_number(no_format):
        """"
        Random phone number will generate phone number based on the no format provided by the user.
        """

        if no_format.upper() == "INDIA":
            phone_number = f"+91-{random.randint(1000,9999 )}-{random.randint(100000,999999)}"
            RandomTestDataGenerator.log.info(f"The random test data utility generated Phone number : {phone_number}")
        elif no_format.upper() == "US":
            phone_number = f"+1 {random.randint(100, 999)}-{random.randint(100, 999)}-{random.randint(1000, 9999)}"
            RandomTestDataGenerator.log.info(f"The random test data utility generated Phone number : {phone_number}")
        else:
            phone_number = fake.phone_number()
            RandomTestDataGenerator.log.info(f"The random test data utility generated Phone number : {phone_number}")

        return phone_number

    @staticmethod
    def get_id(id_format="numeric", chars=string.ascii_uppercase + string.digits, n=6):
        """"
        The random id generator will helps to generate the ID with different format like only digits: 123456789 or alpha numeric
        :param id_format: This the format how the ID should be returned ex: numeric or alpha numeric format
        :param n: lenght of the ID
        :param chars: Character combination
        """
        if id_format.lower() == "alpha_numeric":
            random_id = ''.join(random.choice(chars) for _ in range(n))
            RandomTestDataGenerator.log.info(f"The random test data utility generated ID : {random_id}")
        elif id_format.lower() == "numeric":
            digits = string.digits
            random_id = ''.join(random.choice(digits) for _ in range(n))
            RandomTestDataGenerator.log.info(f"The random test data utility generated ID : {random_id}")
        else:
            RandomTestDataGenerator.log.error("Invalid ID format provided to generate random ID")
            raise Exception("ID format should be alpha_numeric or numeric")

        return random_id

    @staticmethod
    def get_job_type():
        """"
            This method will generate and return the random job type
        """

        return fake.job()

    @staticmethod
    def get_random_string(length):
        """"
            This method will generate and return the random string based on user provided length
            :param length : Length of the random string
        """
        # choose from all lowercase letter
        letters = string.ascii_letters
        result_str = ''.join(random.choice(letters) for i in range(length))
        RandomTestDataGenerator.log.info(f"Random test data utility generated string : {result_str}")
        return result_str

    @staticmethod
    def get_random_number(length):
        """"
            This method will generate and return the random passed based on user provided length
            :param length : Length of the random number
        """
        digits = string.digits
        result_no = ''.join(random.choice(digits) for i in range(length))
        RandomTestDataGenerator.log.info(f"Random test data utility generated string : {result_no}")
        return result_no

    @staticmethod
    def get_random_password(length=12):
        """"
            This method will generate and return the random password based on user provided length
            :param length : Length of the random string
        """
        if length < 12 or length > 15:
            RandomTestDataGenerator.log.error("Random password length should be in between 8 to 15")
            raise Exception("Password length should be between 8 to 15 characters")
        else:
            # characters = string.ascii_letters + string.digits + string.punctuation
            characters = string.ascii_lowercase + string.ascii_uppercase + string.punctuation
            password = ''.join(random.choice(characters) for i in range(length))
            RandomTestDataGenerator.log.info(f"Random test data utility generated password : {password}")
            return password

    @staticmethod
    def random_char(size, chars=string.ascii_lowercase + string.digits):
        return ''.join(random.choice(chars) for x in range(size))

