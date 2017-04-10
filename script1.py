.data
msg1:.asciiz "Please insert text (max 20 characters): "
msg2:.asciiz "\nThe length of the text is: "

newline: .asciiz "\n"

str1: .space 20
.text
.globl main
main:
addi $v0, $v0,4
la $a0,msg1
syscall #print msg1
li $v0,8
la $a0,str1
addi $a1,$zero,20
syscall   #get string 1

la $a0,str1  #pass address of str1
jal len

len: 
## your code here
addi $t2, $zero, 0 # $t2 is what we want to return in the end -- the count of the length of the character array
addi $s1, $zero, 0 # Index i for array traversing | init. to 0 | i = 0

Loop:

add $s1, $s1, $a0 # Adds the location of the index to the location of the base of the array | $t1 is now the location of: array[index]
lw $t0, 0($s1)

beq $t0, $zero, exit
addi $t2, $t2, 1 # Count = Count + 1
addi $s1, $s1, 1 # i = i + 1
j Loop

exit: 
la $a0,msg2 
li $v0,4
syscall
move $a0,$t0 #output the results 
li $v0,1
syscall

li $v0,10
syscall