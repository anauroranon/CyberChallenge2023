0000000000001149 <secret>:
    1149:	f3 0f 1e fa          	endbr64 
    114d:	55                   	push   rbp
    114e:	48 89 e5             	mov    rbp,rsp
    1151:	89 7d ec             	mov    DWORD PTR [rbp-0x14],edi
    1154:	c7 45 fc 20 00 00 00 	mov    DWORD PTR [rbp-0x4],0x20
    115b:	83 7d ec 14          	cmp    DWORD PTR [rbp-0x14],0x14
    115f:	7e 35                	jle    1196 <secret+0x4d>
    1161:	83 6d fc 1e          	sub    DWORD PTR [rbp-0x4],0x1e
    1165:	83 7d ec 32          	cmp    DWORD PTR [rbp-0x14],0x32
    1169:	74 27                	je     1192 <secret+0x49>
    116b:	81 45 fc f4 01 00 00 	add    DWORD PTR [rbp-0x4],0x1f4
    1172:	8b 45 fc             	mov    eax,DWORD PTR [rbp-0x4]
    1175:	01 c0                	add    eax,eax
    1177:	39 45 ec             	cmp    DWORD PTR [rbp-0x14],eax
    117a:	7d 05                	jge    1181 <secret+0x38>
    117c:	d1 65 fc             	shl    DWORD PTR [rbp-0x4],1
    117f:	eb 15                	jmp    1196 <secret+0x4d>
    1181:	8b 45 fc             	mov    eax,DWORD PTR [rbp-0x4]
    1184:	89 c2                	mov    edx,eax
    1186:	c1 ea 1f             	shr    edx,0x1f
    1189:	01 d0                	add    eax,edx
    118b:	d1 f8                	sar    eax,1
    118d:	89 45 fc             	mov    DWORD PTR [rbp-0x4],eax
    1190:	eb 04                	jmp    1196 <secret+0x4d>
    1192:	83 45 fc 3c          	add    DWORD PTR [rbp-0x4],0x3c
    1196:	90                   	nop
    1197:	5d                   	pop    rbp
    1198:	c3                   	ret