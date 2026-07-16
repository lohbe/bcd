# Worked example — 2026-07-16

## Goal
<!-- What concept/skill is today's worked example targeting? -->
ghostty automation

## Approach
<!-- e.g. graph thinking, functional approach, recursion, data structure -->
using applescript to automate ghostty terminal

## Worked example
<!-- The worked example / code goes here or in a sibling file -->
the resulting idempotent script is:

tell application "Ghostty"
	-- 1. Check if the workspace is already running
	-- We search for a terminal whose name contains our specific SSH host or process
	set activeSessions to every terminal whose name contains "zeus.lan"
	
	if (count of activeSessions) > 0 then
		-- The session exists! Bring it to the front and exit the script
		set existingTerm to item 1 of activeSessions
		focus existingTerm
		return
	end if
	
	-- 2. If it doesn't exist, proceed with building the workspace
	
	-- Open a new window (Tab 1)
	set win to new window
	set tab1 to selected tab of win
	set term1 to focused terminal of tab1
	
	-- Create a sub-tab (split) in the first tab
	set term1_sub to split term1 direction right
	
	-- Open Tab 2 in the same window
	set tab2 to new tab in win
	set term2 to focused terminal of tab2
	
	-- Pipe the commands directly into the terminals
	
	-- Tab 2: SSH Session
	input text "ssh ben@zeus.lan -t tmux new -A -s 0" to term2
	send key "enter" to term2
	
	-- Tab 1 (Main): mactop
	input text "mactop" to term1
	send key "enter" to term1
	
	-- Tab 1 (Sub-tab): rapid-mlx
	input text "uvx rapid-mlx serve qwen3.5-122b-mxfp4" to term1_sub
	send key "enter" to term1_sub
end tell

## Reflection
<!-- What did you learn? What was hard? -->
i learnt that it was possible to script a tool that i used, ghostty with macos applescript.
it is not a usual programming language, combined with some limitations and user experience issues, i discovered it is a niche automation method.
