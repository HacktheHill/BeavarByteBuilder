/******************************************************************************************
 *
 *  BBuilder_Scheduler.cpp
 *
 *
 *
 ******************************************************************************************/

/*-----------------------------------------------------------------------------------------
 *  Includes
 *-----------------------------------------------------------------------------------------*/
#include "BB-scheduler.h"
#include "BB-config.h"

#include "Arduino.h"

#include <stdint.h>

/*-----------------------------------------------------------------------------------------
 *  Local Defines
 *-----------------------------------------------------------------------------------------*/
#define BBUILDER_TASK1MS (1U)
#define BBUILDER_TASK10MS (10U)
#define BBUILDER_TASK100MS (100U)

/*-----------------------------------------------------------------------------------------
 *  Local Variables
 *-----------------------------------------------------------------------------------------*/
static uint32_t BBuilder_prevTimeTask1ms = 0;
static uint32_t BBuilder_prevTimeTask10ms = 0;
static uint32_t BBuilder_prevTimeTask100ms = 0;
static uint32_t BBuilder_prevTimeTaskCustomInterval = 0;

/*-----------------------------------------------------------------------------------------
 *  Global Functions
 *-----------------------------------------------------------------------------------------*/
void BB_TaskScheduler(void)
{
#ifdef BB_CONFIG_TASK_1MS_ENABLED
  if (millis() - BBuilder_prevTimeTask1ms >= BBUILDER_TASK1MS)
  {
    BB_Task_1ms();
    BBuilder_prevTimeTask1ms = millis();
  }
#endif
#ifdef BB_CONFIG_TASK_10MS_ENABLED
  if (millis() - BBuilder_prevTimeTask10ms >= BBUILDER_TASK10MS)
  {
    BB_Task_10ms();
    BBuilder_prevTimeTask10ms = millis();
  }
#endif
#ifdef BB_CONFIG_TASK_100MS_ENABLED
  if (millis() - BBuilder_prevTimeTask100ms >= BBUILDER_TASK100MS)
  {
    BB_Task_100ms();
    BBuilder_prevTimeTask100ms = millis();
  }
#endif

#ifdef BB_CONFIG_TASK_CUSTOM_INTERVAL_ENABLED
  if (millis() - BBuilder_prevTimeTaskCustomInterval >= BBUILDER_CONFIG_CUSTOM_INTERVAL_TASK)
  {
    BB_Task_CustomInterval();
    BBuilder_prevTimeTaskCustomInterval = millis();
  }
#endif
}

/*-----------------------------------------------------------------------------------------
 *  Local Functions
 *-----------------------------------------------------------------------------------------*/
