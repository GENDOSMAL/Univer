#include <linux/init.h>
#include <linux/module.h>
#include <linux/kernel.h>
#include <linux/sched.h>  
#include <linux/tty.h> 
#include <linux/sched/signal.h>
#include <linux/string.h>
#include <linux/module.h>
#include <linux/mm.h>
#include <linux/sched.h>
#include <linux/uaccess.h>
#include <linux/delay.h> 
#include <linux/interrupt.h> 

#ifndef DECLARE_TASKLET_OLD 
#define DECLARE_TASKLET_OLD(arg1, arg2) DECLARE_TASKLET(arg1, arg2, 0L) 
#endif 

static void tasklet_fn(unsigned long data) 
{ 
    pr_info("Example tasklet starts\n"); 
    mdelay(5000); 
    pr_info("Example tasklet ends\n"); 
} 

static DECLARE_TASKLET_OLD(mytask, tasklet_fn); 

static __init int hello_init(void)
{
    printk(KERN_ALERT "Module about task 4 loaded\n");
    tasklet_schedule(&mytask); 
    mdelay(200); 
    return 0;
}

static __exit void hello_exit(void)
{
    printk(KERN_ALERT "Module about task 4 unloaded!\n");
    tasklet_kill(&mytask); 
}

module_init(hello_init);
module_exit(hello_exit);

MODULE_DESCRIPTION("LAB4 Malkerov GA");
MODULE_LICENSE("GPL");