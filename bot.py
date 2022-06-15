import random
import time
import sys
import pyperclip
def dynamic_print(data, percent):
    print('#### '+ str(data).zfill(7) + ', ', \
          str(round(percent*100, 1)).zfill(4), end = '% ')
def trigram(word_count, last_word = ''):
    totaltext = ''
    try:
        with open('document.txt') as f:
           things = f.read()
           for i in range(things.count('(')):
               start = things.find( '(' )
               end = things.find( ')' )
               if things[end+1] == '.' or things[end+2] == '.'\
                  or things[end+1] == '"' or things[end+1] == "'"\
                  or things[end+1] == '-' or things[end+1] == ':'\
                  or things[end+1] == '(' or things[end+1] == ')'\
                  or things[end+1] == '%' or things[end+1] == '”':
                   result = things[start:end+1]
               else:
                   result = things[start:end+2]
               things = things.replace(result, '')
           things = ''.join(i for i in things if not i.isdigit()).split()
           starttime = time.time()
           for i in range(len(things)):
               word = things[i]
               try:
                   if word in words:
                       words[word].append(things[i + 1])
                   else:
                       words[word] = [things[i + 1]]
               except:
                   pass
           wordst = {}
           for i in range(len(things)-1):
               wordt = things[i] + ' ' + things[i+1]
               try:
                   if wordt in wordst:
                       wordst[wordt].append(things[i + 2])
                   else:
                       wordst[wordt] = [things[i + 2]]
               except:
                   pass        
           last_word = random.choice(list(wordst.keys()))
           text = last_word
           while len(text.split()) < word_count:
               try:
                   try:
                       if wordst[last_word] != []:
                           next_word = random.choice(wordst[last_word])
                           floatingvar = last_word.split()
                           last_word = floatingvar[1] + ' ' + next_word
                           text += ' ' + floatingvar[1] + ' '
                       else:
                           next_word = random.choice(words[last_word])
                           last_word = next_word
                           text += ' ' + last_word + ' '
                   except:
                       next_word = random.choice(words[last_word])
                       last_word = next_word + random.choice(words[next_word])
                       text += ' ' + last_word + ' '
               except Exception as e:
                   raise e
    except Exception as e:
        raise e 
    text = text.replace(' .', '.')
    text = text.replace(' ,', ',')
    text = text.replace('.,', ',')
    text = text.replace('"', '')
    text = text.replace('(', '')
    text = text.replace(')', '')
    text = text.replace('“', '')
    text = text.replace('”', '')
    text = text.replace('*', '')
    text = text.replace('-- ', '')
    text = text.replace('-', ' ')
    text = text.replace('$', '')
    text = text.replace('%', '')
    text = text.split()
    text[1] = ''
    text = ' '.join(text)
    text = text[text.find('.')+2:text.rfind('.')+1]
    text = text.replace(' .', '.')
    newtext = '\t'
    for i in text:
        if i == '.':
            if random.randint(1, 12) == 10:
                i = '.\n\n\t'
        newtext = newtext + i
    return newtext
while True:
    word_count = input('------------------\nWord count: ')
    if word_count == '':
        word_count = 100
    else:
        word_count = int(word_count)
    print('Estimated time:', str(0.000000054*word_count**2+(0.0003*word_count)), 'seconds')
    starttime = time.time()
    totaltext = ''
    for i in range (word_count//1000):
        if i == 0:
            totaltext += trigram(1000, 'in particular.')
        else:
            if i%10 == 0:
                dynamic_print(str(i*1000), i*1000/word_count)
            thing = totaltext.split()
            totaltext += '\n\n'+trigram(1000, ' '.join(thing[len(thing)-2:len(thing)]))
    thing = totaltext.split()
    if word_count > 1000:
        totaltext += '\n\n'+trigram(word_count%1000, ' '.join(thing[len(thing)-2:len(thing)]))
    else:
        totaltext += '\n\n'+trigram(word_count%1000, ' '.join(thing[len(thing)-2:len(thing)])) 
    print('\nCopied to clipboard!')
    pyperclip.copy(totaltext)
    print('Time:', str(time.time()-starttime))   
    
