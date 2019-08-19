import logging
import enum_policies


def main():
    logging.basicConfig(filename='main.log', level=logging.INFO)
    logging.info('Started')
    enum_policies.enumerate_sec_rules()
    enum_policies.enumerate_nat_rules()
    logging.info('Finished')


if __name__ == '__main__':
    main()
