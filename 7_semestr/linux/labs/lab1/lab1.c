#include <linux/init.h>
#include <linux/module.h>
#include <linux/kernel.h>
#include <linux/sched.h>  
#include <linux/tty.h> 

static void print_string(char *str) 
{ 
 struct tty_struct *my_tty = get_current_tty(); 
 if (my_tty) { 
    const struct tty_operations *ttyops = my_tty->driver->ops; 
    (ttyops->write)(my_tty, str, strlen(str)); 
    (ttyops->write)(my_tty, "\015\012", 2); 
 } 
} 

static __init int hello_init(void)
{
    print_string("Hello,teminal!");
    printk(KERN_ALERT "Hello,kernel\n");
    return 0;
}

static __exit void hello_exit(void)
{
    print_string("Goodbye,teminal!");
    printk(KERN_ALERT "Goodbye,Kernel!\n");
}


module_init(hello_init);
module_exit(hello_exit);

MODULE_DESCRIPTION("DDDD");
MODULE_LICENSE("GPL");