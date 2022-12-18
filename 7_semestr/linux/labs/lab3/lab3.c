#include <linux/init.h>
#include <linux/module.h>
#include <linux/kernel.h>
#include <linux/sched.h>  
#include <linux/tty.h> 
#include <linux/sched/signal.h>
#include <linux/string.h>
#include <linux/module.h>
#include <linux/mm.h>
#include <asm/pgtable.h>
#include <linux/sched.h>
#include <linux/uaccess.h>

static __init int hello_init(void)
{
    printk(KERN_ALERT "Module about task 3 loaded\n");
    struct task_struct *task = current;
    struct mm_struct *mm = task->mm;
    unsigned long vm_start = mm->start_code;
    unsigned long p_start = __pa(vm_start);
    pgd_t *pgd;
    p4d_t *p4d;
    pud_t *pud;
    pmd_t *pmd;
    pte_t *pte;
    pgd = pgd_offset(mm, vm_start);
    p4d = p4d_offset(pgd, vm_start);
    pud = pud_offset(p4d, vm_start);
    pmd = pmd_offset(pud, vm_start);
    pte = pte_offset_map(pmd, vm_start);
    unsigned long user = pte_flags(*pte) & _PAGE_USER;
    unsigned long dirty = pte_flags(*pte) & _PAGE_DIRTY;

    printk("Virtual address: 0x%lx\n"
        "Physical address: 0x%lx\n"
        "young: 0x%lx\n"
        "dirty: 0x%lx\n"
        "write: 0x%lx\n"
        "user: 0x%lx\n",
       vm_start, p_start,pte_dirty(*pte),dirty,pte_write(*pte),user);

    return 0;
}

static __exit void hello_exit(void)
{
    printk(KERN_ALERT "Module about task 3 unloaded!\n");
}


module_init(hello_init);
module_exit(hello_exit);

MODULE_DESCRIPTION("LAB3 Malkerov GA");
MODULE_LICENSE("GPL");