import hydra
from omegaconf import DictConfig, OmegaConf

from process_data import process_data
from segment import segment


@hydra.main(config_path="../config", config_name="config")
def main(config: DictConfig):

    if config.flow == "all":
        print('--- Tratamentos dos dados de treino INICIADOS ---')
        process_data(config)
        print('--- Tratamentos dos dados de treino FINALIZADOS ---')
        
        print('--- Treinamento do modelo INICIADO ---')
        segment(config)
        print('--- Treinamento do modelo FINALIZADO ---')

    elif config.flow == "process_data":
        print('--- Tratamentos dos dados de treino INICIADOS ---')
        process_data(config)
        print('--- Tratamentos dos dados te treino FINALIZADOS ---')

    elif config.flow == "segment":
        print('--- SOMENTE Treinamento do modelo INICIADO ---')
        segment(config)
        print('--- Treinamento do modelo FINALIZADO ---')

    else:
        print("flow not found")


if __name__ == "__main__":
    main()