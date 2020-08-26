import pygame
import random
import time
pygame.init()
color0=(200,200,255)
num_operations=[0]
font1=pygame.font.Font(None,30)
def insertion(surface0,arr,speed):
    n=750//len(arr)
    ar=[int((i/max(arr))*450) for i in arr]
    wtime=(100-speed)*5
    for i in range(len(ar)):
        pygame.draw.rect(surface0,color0,(75+i*n,75,n,ar[i]))
    pygame.time.wait(wtime)
    
    for j in range(len(ar)):
        min_e=ar[j]
        num_operations[0]+=1
        for k in range(j,-1,-1):
            num_operations[0]+=1
            for i in range(len(ar)):
                pygame.draw.rect(surface0,color0,(75+i*n,75,n,ar[i]))
                text=font1.render("number of operations: "+str(num_operations[0]),True,(240,240,240))
                surface0.blit(text,(400,20))
            for events in pygame.event.get():
                if events.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            pygame.draw.rect(surface0,(0,0,255),(75+j*n,75,n,ar[j]))
            if ar[k]>min_e:
                ar[k+1],ar[k]=ar[k],ar[k+1]
                num_operations[0]+=1
                pygame.draw.rect(surface0,(255,0,0),(75+(k+1)*n,75,n,ar[k+1]))
                
            pygame.time.wait(int(wtime/10))
            pygame.display.update()
            surface0.fill((0,0,0))
            
    for g in range(len(ar)):
        pygame.draw.rect(surface0,color0,(75+g*n,75,n,ar[g]))
    text=font1.render("number of operations: "+str(num_operations[0]),True,(240,240,240))
    surface0.blit(text,(400,20))
    pygame.display.update()
    running =True
    while running:
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                pygame.quit()
                quit()
                
        

def merge(surface0,arr,speed):
    n=750//len(arr)
    ar=[int((i/max(arr))*450) for i in arr]
    wtime=(100-speed)*5
    for g in range(len(ar)):
        pygame.draw.rect(surface0,(255,255,255),(75+g*n,75,n,ar[g]))
    pygame.time.wait(int(wtime/10))

    def merge0(ar,l,q,r):
        l1=ar[l:q+1]
        r1=ar[q+1:r+1]
        i,j,k=0,0,l
        while i<len(l1) and j<len(r1):
            if l1[i]<=r1[j]:
                ar[k]=l1[i]
                i+=1
            else:
                ar[k]=r1[j]
                j+=1
            k+=1
            num_operations[0]+=1
            for g in range(len(ar)):
                pygame.draw.rect(surface0,color0,(75+g*n,75,n,ar[g]))
            text=font1.render("number of operations: "+str(num_operations[0]),True,(240,240,240))
            surface0.blit(text,(400,20))
            pygame.display.update()
            pygame.time.wait(int(wtime/10))
            surface0.fill((0,0,0))
            for events in pygame.event.get():
                if events.type == pygame.QUIT:
                    pygame.quit()
                    quit()
        while i<len(l1):
            ar[k]=l1[i]
            i+=1
            k+=1
            num_operations[0]+=1
        while j<len(r1):
            ar[k]=r1[j]
            j+=1
            k+=1
            num_operations[0]+=1
    def mergeSort(ar,l,r):
        num_operations[0]+=1
        for g in range(len(ar)):
            pygame.draw.rect(surface0,color0,(75+g*n,75,n,ar[g]))
        text=font1.render("number of operations: "+str(num_operations[0]),True,(240,240,240))
        surface0.blit(text,(400,20))
        pygame.display.update()
        pygame.time.wait(int(wtime/10))
        surface0.fill((0,0,0))
        
        if l<r:
            q=(l+r)//2
            
            mergeSort(ar,l,q)
            mergeSort(ar,q+1,r)
            merge0(ar,l,q,r)
    mergeSort(ar,0,len(ar))
    surface0.fill((0,0,0))
    for g in range(len(ar)):
        pygame.draw.rect(surface0,color0,(75+g*n,75,n,ar[g]))
    text=font1.render("number of operations: "+str(num_operations[0]),True,(240,240,240))
    surface0.blit(text,(400,20))
    running =True
    while running:
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                pygame.quit()
                quit()
    

def bubble(surface0,arr,speed):
    n=750//len(arr)
    ar=[int((i/max(arr))*450) for i in arr]
    wtime=(100-speed)*5
    for i in range(len(ar)):
        pygame.draw.rect(surface0,color0,(75+i*n,75,n,ar[i]))
    pygame.time.wait(wtime)

    swap=True
    while swap:
        swap=False
        for i in range(len(ar)-1):
            num_operations[0]+=1
            for g in range(len(ar)):
                pygame.draw.rect(surface0,color0,(75+g*n,75,n,ar[g]))
            text=font1.render("number of operations: "+str(num_operations[0]),True,(240,240,240))
            surface0.blit(text,(400,20))
            pygame.draw.rect(surface0,(255,0,0),(75+i*n,75,n,ar[i]))
            pygame.draw.rect(surface0,(0,0,255),(75+(i+1)*n,75,n,ar[i+1]))
            
            pygame.display.update()
            pygame.time.wait(int(wtime))
            surface0.fill((0,0,0))
            if ar[i]>ar[i+1]:
                num_operations[0]+=1
                ar[i],ar[i+1]=ar[i+1],ar[i]
                swap=True
                for g in range(len(ar)):
                    pygame.draw.rect(surface0,color0,(75+g*n,75,n,ar[g]))
                text=font1.render("number of operations: "+str(num_operations[0]),True,(240,240,240))
                surface0.blit(text,(400,20))
                for events in pygame.event.get():
                    if events.type == pygame.QUIT:
                        pygame.quit()
                        quit()
                pygame.draw.rect(surface0,(255,0,0),(75+(i+1)*n,75,n,ar[i+1]))
                pygame.draw.rect(surface0,(0,0,255),(75+i*n,75,n,ar[i]))
                pygame.display.update()
                pygame.time.wait(int(wtime))
            surface0.fill((0,0,0))
    for g in range(len(ar)):
        pygame.draw.rect(surface0,color0,(75+g*n,75,n,ar[g]))
    text=font1.render("number of operations: "+str(num_operations[0]),True,(240,240,240))
    surface0.blit(text,(400,20))
    pygame.display.update()
    running =True
    while running:
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                pygame.quit()
                quit()
    

def quick(surface0,arr,speed):
    n=750//len(arr)
    ar=[int((i/max(arr))*450) for i in arr]
    wtime=(100-speed)*5
    for i in range(len(ar)):
        pygame.draw.rect(surface0,color0,(75+i*n,75,n,ar[i]))
    pygame.time.wait(100)
    def partition(ar,l,r):
        p=ar[r]
        i=l-1

        for j in range(l,r):
            num_operations[0]+=1
            if ar[j]<=p:
                i+=1
                ar[i],ar[j]=ar[j],ar[i]
            for g in range(len(ar)):
                pygame.draw.rect(surface0,color0,(75+g*n,75,n,ar[g]))
            text=font1.render("number of operations: "+str(num_operations[0]),True,(240,240,240))
            surface0.blit(text,(400,20))
            pygame.display.update()
            pygame.time.wait(int(wtime/10))
            surface0.fill((0,0,0))
            for events in pygame.event.get():
                if events.type == pygame.QUIT:
                    pygame.quit()
                    quit()
        ar[i+1],ar[r]=ar[r],ar[i+1]
        return i+1

    def quickSort(ar,l,r):
        num_operations[0]+=1
        for g in range(len(ar)):
             pygame.draw.rect(surface0,color0,(75+g*n,75,n,ar[g]))
        text=font1.render("number of operations: "+str(num_operations[0]),True,(240,240,240))
        surface0.blit(text,(400,20))
        pygame.display.update()
        pygame.time.wait(int(wtime/10))
        surface0.fill((0,0,0))
        if l<r:
            q=partition(ar,l,r)
            quickSort(ar,l,q-1)
            quickSort(ar,q+1,r)
    quickSort(ar,0,len(ar)-1)
    for g in range(len(ar)):
        pygame.draw.rect(surface0,color0,(75+g*n,75,n,ar[g]))
    text=font1.render("number of operations: "+str(num_operations[0]),True,(240,240,240))
    surface0.blit(text,(400,20))
    pygame.display.update()
    running =True
    while running:
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                pygame.quit()
                quit()
    

def heap(surface0,arr,speed):
    n=750//len(arr)
    ar=[int((i/max(arr))*450) for i in arr]
    wtime=(100-speed)*5

    def heapify(ar,i,an):
        num_operations[0]+=1
        l=(2*i)+1
        r=(2*i)+2
        maxe=i
        for g in range(len(ar)):
            pygame.draw.rect(surface0,color0,(75+g*n,75,n,ar[g]))
        text=font1.render("number of operations: "+str(num_operations[0]),True,(240,240,240))
        surface0.blit(text,(400,20))
        pygame.display.update()
        pygame.time.wait(int(wtime/10))
        surface0.fill((0,0,0))
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                pygame.quit()
                quit()
        if l<an and ar[l]>ar[i]:
            num_operations[0]+=1
            maxe=l
            
        if r<an and ar[r]>ar[maxe]:
            num_operations[0]+=1
            maxe=r
        
        if maxe!=i:
            ar[i],ar[maxe]=ar[maxe],ar[i]
            num_operations[0]+=1
            heapify(ar,maxe,an)

    def heapsort(ar):
        an=len(ar)
        for i in range(int(len(ar)/2),-1,-1):
            num_operations[0]+=1
            for g in range(len(ar)):
                pygame.draw.rect(surface0,color0,(75+g*n,75,n,ar[g]))
            text=font1.render("number of operations: "+str(num_operations[0]),True,(240,240,240))
            surface0.blit(text,(400,20))
            pygame.display.update()
            pygame.time.wait(int(wtime/10))
            surface0.fill((0,0,0))
            
            heapify(ar,i,an)
            
        for i in range(an-1,0,-1):
            num_operations[0]+=1
            for g in range(len(ar)):
                pygame.draw.rect(surface0,color0,(75+g*n,75,n,ar[g]))
            text=font1.render("number of operations: "+str(num_operations[0]),True,(240,240,240))
            surface0.blit(text,(400,20))
            pygame.display.update()
            pygame.time.wait(int(wtime/10))
            surface0.fill((0,0,0))
            
            ar[0],ar[i]=ar[i],ar[0]
            an-=1
            heapify(ar,0,an)
        for g in range(len(ar)):
            pygame.draw.rect(surface0,color0,(75+g*n,75,n,ar[g]))
        pygame.display.update()
        pygame.time.wait(int(wtime/10))
        surface0.fill((0,0,0))
    heapsort(ar)
    for g in range(len(ar)):
        pygame.draw.rect(surface0,color0,(75+g*n,75,n,ar[g]))
    text=font1.render("number of operations: "+str(num_operations[0]),True,(240,240,240))
    surface0.blit(text,(400,20))
    pygame.display.update()
    running =True
    while running:
        for events in pygame.event.get():
            if events.type == pygame.QUIT:
                pygame.quit()
                quit()
    

