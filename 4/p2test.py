import unittest
import p2

class TestP2(unittest.TestCase):

    def test_validate_byr(self):
        self.assertTrue(p2.validate_byr(1920))
        self.assertTrue(p2.validate_byr(2002))
        self.assertTrue(p2.validate_byr(1990))
        self.assertFalse(p2.validate_byr(1919))
        self.assertFalse(p2.validate_byr(2003))
        self.assertRaises(ValueError, p2.validate_byr, 'asdf')

    def test_validate_iyr(self):
        self.assertTrue(p2.validate_iyr(2010))
        self.assertTrue(p2.validate_iyr(2020))
        self.assertTrue(p2.validate_iyr(2015))
        self.assertFalse(p2.validate_iyr(2000))
        self.assertFalse(p2.validate_iyr(2022))
        self.assertRaises(ValueError, p2.validate_iyr, 'asdf')

    def test_validate_eyr(self):
        self.assertTrue(p2.validate_eyr(2020))
        self.assertTrue(p2.validate_eyr(2030))
        self.assertTrue(p2.validate_eyr(2025))
        self.assertFalse(p2.validate_eyr(2000))
        self.assertFalse(p2.validate_eyr(2032))
        self.assertRaises(ValueError, p2.validate_eyr, 'asdf')

    def test_validate_hgt(self):
        self.assertTrue(p2.validate_hgt('150cm'))
        self.assertTrue(p2.validate_hgt('193cm'))
        self.assertTrue(p2.validate_hgt('170cm'))
        self.assertTrue(p2.validate_hgt('59in'))
        self.assertTrue(p2.validate_hgt('76in'))
        self.assertTrue(p2.validate_hgt('66in'))
        self.assertFalse(p2.validate_hgt('140cm'))
        self.assertFalse(p2.validate_hgt('200cm'))
        self.assertFalse(p2.validate_hgt('50in'))
        self.assertFalse(p2.validate_hgt('80in'))
        self.assertFalse(p2.validate_hgt('97'))
        self.assertFalse(p2.validate_hgt('asdf'))

    def test_validate_hcl(self):
        self.assertTrue(p2.validate_hcl('#000000'))
        self.assertTrue(p2.validate_hcl('#ffffff'))
        self.assertTrue(p2.validate_hcl('#0aa39d'))
        self.assertFalse(p2.validate_hcl('asdf'))
        self.assertFalse(p2.validate_hcl('#0000000'))
        self.assertFalse(p2.validate_hcl('#1111fg'))
        self.assertFalse(p2.validate_hcl('#FFFFFF'))
        
    def test_validate_ecl(self):
        self.assertTrue(p2.validate_ecl('amb'))
        self.assertTrue(p2.validate_ecl('blu'))
        self.assertTrue(p2.validate_ecl('brn'))
        self.assertTrue(p2.validate_ecl('gry'))
        self.assertTrue(p2.validate_ecl('grn'))
        self.assertTrue(p2.validate_ecl('hzl'))
        self.assertTrue(p2.validate_ecl('oth'))
        self.assertFalse(p2.validate_ecl('aaa'))

    def test_validate_pid(self):
        self.assertTrue(p2.validate_pid('000000001'))
        self.assertTrue(p2.validate_pid('999999999'))
        self.assertFalse(p2.validate_pid('11111111a'))
                                        
    def test_validate_field(self):
        self.assertTrue(p2.validate_field('ecl', 'hzl'))
        
if __name__ == '__main__':
    unittest.main()
    
