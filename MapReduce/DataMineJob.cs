using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Microsoft.Hadoop;
using Microsoft.Hadoop.MapReduce;
using Microsoft.Hadoop.MapReduce.Json;

namespace OneDirDataMining
{
    class DataMineJob: HadoopJob<DataMineMapper, DataMineReducer>
    {
        public override HadoopJobConfiguration Configure(ExecutorContext context)
        {
            var config = new HadoopJobConfiguration();
            config.InputPath = "input/logs";
            config.OutputFolder = "output/logOut";
            return config;
        }
    }

    class DataMineMapper : JsonInMapperBase<LogRecord>
    {
        public override void Map(LogRecord value, MapperContext context)
        {


            context.EmitKeyValue(value.Action, "1");
            context.EmitKeyValue(value.User, "1");
            context.EmitKeyValue(value.HTTP, "1");
        }
    }

    class DataMineReducer : ReducerCombinerBase
    {
        public override void Reduce(string key, IEnumerable<string> values, ReducerCombinerContext context)
        {
            int count = 0;
            foreach (string value in values)
            {
                count += int.Parse(value);
            }
            context.EmitKeyValue(key, count.ToString());
        }
    }
}
