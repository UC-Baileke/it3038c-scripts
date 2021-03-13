$Machines = 'Baileke-win'
$logfile = "c:\logs\counterdata.log"

foreach ($Machine in $Machines) {
    #$RCounters = get-counter -ListSet * -ComputerName $Machine
    #"There are {0} counters on {1}" -f $RCounters.count, ($Machine)

    $pt = (get-counter -counter "\Processor(_Total)\% Processor Time" -SampleInterval 1 -MaxSamples 5).CounterSamples.CookedValue
    $sample = 1
    foreach ($p in $pt) {
        "Sample {2}: CPU is at {0}% on {1}" -f [int]$p, $Machine, $sample | Out-File -Append $logfile
        $sample++
    }
    
}