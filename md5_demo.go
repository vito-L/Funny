package main

import (
	"crypto/md5"
	"fmt"
	"log"
	"os"
	//"io/ioutil"
)

func main() {
	defer func() {
		if err := recover(); err != nil {
			fmt.Println("请输入需要加密的字符串，如：./md5Go 123")
		}
	}()
	if os.Args[1] == "help" {
		fmt.Println("使用帮助:\nhelp\t查看帮助信息\n./md5Go 123\t123为需要加密的字符串")
	} else {
		data := []byte(os.Args[1])
		//if err != nil{
		//    log.Fatal(err)
		//}
		fmt.Printf("text: %s\tmd5: %x\n", os.Args[1], md5.Sum(data))
		logtext := fmt.Sprintf("text: %s\tmd5: %x\n", os.Args[1], md5.Sum(data))
		logFile, _ := os.OpenFile("./md5History.txt", os.O_CREATE|os.O_WRONLY|os.O_APPEND, 0666)
		//logFile,_ := os.Create("./md5History.txt")
		//if err != nil{
		//    log.Println(err)
		//}
		Info := log.New(logFile, "[info] ", log.Ldate|log.Ltime)
		Info.SetFlags(log.Ldate | log.Ltime)
		Info.SetPrefix("[info] ")
		Info.Output(2, logtext)
	}
}
