# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
#MISC
LED_VERDE = 3 #o
LED_VERMELHO = 13 #o
BUTTON_IN = 40 #i
#OUT
TX_OUT = 15
GND_OUT = 19
RX_OUT = 21
#IN
TX_IN = 33
GND_IN = 31
RX_IN = 29
# END pin Defines
#inputs lists
CONNECTIONS = [TX_IN, GND_IN, RX_IN, TX_OUT, GND_OUT, RX_OUT]
# - - - - -
# > Setups
#MISC
GPIO.setup(LED_VERDE,GPIO.OUT)
GPIO.setup(LED_VERMELHO,GPIO.OUT)
GPIO.setup(BUTTON_IN, GPIO.IN, pull_up_down = GPIO.PUD_UP)
#IN
GPIO.setup(TX_OUT,GPIO.IN,pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(GND_OUT,GPIO.IN,pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(RX_OUT,GPIO.IN,pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(TX_IN,GPIO.IN,pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(GND_IN,GPIO.IN,pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(RX_IN,GPIO.IN,pull_up_down = GPIO.PUD_DOWN)
# Set all GPIO to INPUT
# End Setup

'''
    @brief  Testa a conexão do Ponto A para um ou mais Pontos B
    
    @note   Para utilizar essa função é necessário definir uma LIST chamada CONNECTIONS,
            em escopo global, que contém todos os pontos que serão testados
            
    @note   É necessário que todos os pontos estejam definidos como INPUT no
            setup com pull down ativado. Esta função altera os INPUTs automaticamente
            para testar cada pino, colocando o Ponto A como OUTPUT
    
    @param  PointA  Especifica o Ponto A que será verificado o curto, este ponto é
                    colocado em nível alto e definido como OUTPUT automaticamente
                    pela função. Este parâmetro deve ser inserido como uma LIST com
                    apenas UM parâmetro
            
            PointB  Especifica o(s) Ponto(s) B que será verificado se o sinal chegou.
                    Este parâmetro deve ser inserido como uma LIST mesmo se houver apenas,
                    um parâmetro
        
    @retval Booleano True ou False

'''




def TestPins(PointA, PointB):
    
    GPIO.setup(PointA, GPIO.OUT)
    GPIO.output(PointA, GPIO.HIGH)
    #PointA como output e em nivel alto
    
    pass_flag = True;
    #flag que indica se o teste passou
    
    
    TESTPINS = CONNECTIONS
    
    #TESTPINS.remove (PointA)
    # Retira do teste o pino output
    
    for pin in PointB:
        TESTPINS.remove (pin)
        #print (str (TESTPINS))
    for pin in PointA:
        TESTPINS.remove (pin)
        #print (str (TESTPINS))
    # Retira do primeiro teste os pinos que deveriam estar em curto
    
    print ("PointA: " + str(PointA)) 
    print ("PointB: " + str(PointB))
    print ("\n")
    
    print ("Pinos que não devem ocorrer: " + str(TESTPINS) + "\n")
    
    print ("Nao devem ocorrer:")
    for pin in TESTPINS:
        if GPIO.input (pin):
            print ("Pin " + str(pin) + " conectado a " + str(PointA))
            pass_flag = False
        else:
            print ("Pin " + str(pin) + " nao conectado a " + str(PointA))
    #Verificando as conexões que não podem ocorrer
     
    print ("\n")
    
    print ("Devem ocorrer:")

    for pin in PointB:         
        if GPIO.input (pin):
            print ("Pin " + str(pin) + " conectado a " + str(PointA))
            
        else:
            print ("Pin " + str(pin) + " nao conectado a " + str(PointA))
            pass_flag = False
    #Verifica as conexões que tem que ocorrer
    for pin in PointB:
        TESTPINS.append (pin)
       # print (str (TESTPINS))
    for pin in PointA:
        TESTPINS.append (pin)
       # print (str (TESTPINS))  
    
    print ("TESTPINS " + str(TESTPINS))
    GPIO.setup(PointA ,GPIO.IN,pull_up_down = GPIO.PUD_DOWN)
    
    if pass_flag:
        return True
    else:
        return False

                             

def kkVmgpioTest2():
    pass_flag = True;
    
    if TestPins ([TX_OUT], [TX_IN]) == False:
        pass_flag = False
    if TestPins ([GND_OUT], [GND_IN]) == False:
        pass_flag = False
    if TestPins ([RX_OUT], [RX_IN]) == False:
        pass_flag = False
    
    if pass_flag:
        return True
    return False
    

def testFailed():
    GPIO.output(LED_VERMELHO,1)
    GPIO.output(LED_VERDE,0)
    time.sleep(2)
    GPIO.output(LED_VERMELHO,0)
    GPIO.output(LED_VERDE,0)
    print ("Failed")
# End testFailed
#
def testSuccess():
    GPIO.output(LED_VERMELHO,0)
    GPIO.output(LED_VERDE,1)
    time.sleep(2)
    GPIO.output(LED_VERMELHO,0)
    GPIO.output(LED_VERDE,0)
    print("Success")
# End testSuccess
#
#
#
#


while(1):
    if(GPIO.input(BUTTON_IN) == 0):
    #if (input()):
        print ("Novo teste:")
        if kkVmgpioTest2() == False:
            testFailed()
        else:
            testSuccess()
        print("\n\n\n")
# End while(1)

