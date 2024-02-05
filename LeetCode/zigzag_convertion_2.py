import math


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        arr = []
        s_editing = s
        number_in_iteration = 0
        while(len(s_editing) > 0):
            if number_in_iteration == 0:
                arr.append(s_editing[0:numRows])
                s_editing = s_editing[numRows:len(s)]
            else:
                arr.append(s_editing[0:1])
                s_editing = s_editing[1:len(s)]
            number_in_iteration += 1
            if number_in_iteration == numRows:
                number_in_iteration == 0

        return arr

    def quantity_of_cols(self, s, numRows):
        counter_cols = 0
        number_in_iteration = 0
        len_str = len(s)
        while(len_str > 0):
            if number_in_iteration == 0:
                len_str -= numRows
                counter_cols +=1
            else:
                len_str -= 1
                counter_cols +=1
            number_in_iteration += 1
            if number_in_iteration == numRows:
                number_in_iteration == 0

        return counter_cols


solution = Solution()
print(
    solution.convert(
        "rrxtvodtzzduonaigmfdalyzeocxsmmmflfablvckbwyoxjvloalbamfppehdrvieblgmgiyhhxygivtwvfzvtgmikwndryisjqeradzhczpmujirqjojpbuzxhdohnjqdpkdulnykekgnszddnpsojsnsxeaknspecuznjxzoifbcehguwykfsyzrezdtusxwpwmywnmgvqizxqvtrgajgzdmbgfvzctobhozvdfqtnrsgnlxvnidmlppsukryghbnxaiafyvvqnbfyyangfasurmqcfoimsxlsgmaghvwxydvyflgknaeemugrlqfdorxwfzcoubluejskubuhbbloxuhimnnagnynmbbjcndiwyssbpzcqmsniayvpnxxawknxlybadjybeqctrhlgzyobyjsmjpmfzbenzfndqmguelnwsyetzsxzeplnfasgdytddhitvqqzbfxvgbrfwogadspkujrxhkcmtkhobxqedncjrtqpjwroqgzkpqiwckkwxrkapaeuqidhdvymrpdkvcumuekwpuumlfmahsuxdzgguevotayocscyxmwogrcswqufkrdnqlwnqtbjtbaxvcvuprixikpgckondravcyiurlgkoghkkeebypzizqpccdrfwtbaslvjxbwljfxvmczkrassqjwvonakhdnbpkmolkbwqztcbumuugonqlieaipjoekdoxrbhszzrsduprqjyfyosgssrjcfnmidlbettdunyyjnpayphxdzfyrwjvdxilcvohqimlxklgzciyspxxqcvibfdeensgjgpzqcmnoxwoagouylroppyquevarnictyemaqzoqxesesmcffsxurnqvkqozztvxxhzpiphguz",
        399,
    )
)
