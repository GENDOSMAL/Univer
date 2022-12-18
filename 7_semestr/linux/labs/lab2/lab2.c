#include <linux/init.h>
#include <linux/module.h>
#include <linux/kernel.h>
#include <linux/sched.h>  
#include <linux/tty.h> 
#include <linux/sched/signal.h>
#include <linux/string.h>


static void  print_terminal(char *str,bool neewString) 
{ 
 struct tty_struct *my_tty = get_current_tty(); 
 if (my_tty) { 
    const struct tty_operations *ttyops = my_tty->driver->ops; 
    (ttyops->write)(my_tty, str, strlen(str)); 
    if(neewString)
        (ttyops->write)(my_tty, "\015\012", 2); 
 } 
} 

static __init int hello_init(void)
{
    printk(KERN_ALERT "Module about task 2 loaded\n");
    printk(KERN_INFO "Current process ID:%d\n",current->pid);
    printk(KERN_INFO "Parent process ID:%d\n",current->real_parent->pid);

    char buffer[512];
    sprintf(buffer,"Current process ID: %d",current->pid);
    print_terminal(buffer,true);
    sprintf(buffer,"Parent process ID: %d",current->real_parent->pid);
    print_terminal(buffer,true);

    struct task_struct *task = current;
    int parentProcessCount=0;
    while (task->real_parent != task) {
        parentProcessCount=parentProcessCount+1;
        printk(KERN_ALERT "Parent process ID: %d\n", task->real_parent->pid);
        int i=0;
        for(i=0;i<parentProcessCount;i++){
            print_terminal("\t",false);
        }
        sprintf(buffer,"->%d",task->real_parent->pid);
        print_terminal(buffer,true);
        task = task->real_parent;
        
    }

    return 0;
}

static __exit void hello_exit(void)
{
    printk(KERN_ALERT "Module about task 2 unloaded!\n");
}


module_init(hello_init);
module_exit(hello_exit);

MODULE_DESCRIPTION("LAB2 Malkerov GA");
MODULE_LICENSE("GPL");