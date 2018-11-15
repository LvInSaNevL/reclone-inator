#NoEnv  ; Recommended for performance and compatibility with future AutoHotkey releases.
; #Warn  ; Enable warnings to assist with detecting common errors.
SendMode Input  ; Recommended for new scripts due to its superior speed and reliability.
SetWorkingDir %A_ScriptDir%  ; Ensures a consistent starting directory.


; Closes AHK Script
<^#esc::ExitApp


; Display all key codes
<^#LShift::
HelpArr := ["Ctrl, Win, Esc: Closes current AHK script"
		,"Ctrl, Win, Shift: Displays this message"
		,"Ctrl, Win, Space: Google searches highlighted text"
		,"Ctrl, Win, Q: Autocompletes link"]
Loop % HelpArr.MaxIndex()
	Content .= HelpArr[A_Index] "`n"
Msgbox % Content
return

; Ctrl + Space google search copied value when no full screen apps
<^#space::
Gosub Check_FullScreenActive
If !(FullScreenActive) {
	Send,^c
	ClipWait
	Run, http://www.google.com/search?q=%Clipboard%
}	
return

; Autocompletes Link
<^#Q::
Gosub Check_FullScreenActive
If !(FullScreenActive) {
	Send, ^x
	LinkString = https://www.%Clipboard%.com
	ClipWait
	SendInput % LinkString
}
return

; Global Media Keys


; Check if full screen
Check_FullScreenActive:
wingetpos,,,w,h,A
wwwh=%w%%h%
swsh=%a_screenwidth%%a_screenheight%
WinGet, Style, Style, A
FullScreenActive := false
if !(Style & 0xC00000) {
	if(wwwh = swsh) {
		FullScreenActive := true
	}
}
return

; Autocompletion ( https://github.com/dwyl/english-words )
String := ""