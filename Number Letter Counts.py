nums_dict = {100: 'hundred',1000:'thousand'}
nums_20_90 = ['Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
nums_0_19 = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', "Nine", 'Ten',
            'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen','Nineteen']
            
def num2words(num):
    if num < 20:
        return nums_0_19[num]
    if num < 100:
        return nums_20_90[num / 10 - 2] + ('' if num % 10 == 0 else '' + nums_0_19[num % 10])

    maxkey = max([key for key in nums_dict.keys() if key <= num])
    return num2words(num/maxkey) + '' + nums_dict[maxkey] + ('' if num % maxkey == 0 else 'and' + num2words(num % maxkey))

totalLetterCount = sum([len(num2words(x)) for x in range(1, 1000 + 1)])
print(totalLetterCount)