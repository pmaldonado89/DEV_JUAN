import api from '../api/axios';
import { Miner } from '../interfaces/Miner';

export const getAllMiners = async (): Promise<Miner[]> => {
    const response = await api.get('/miners');
    return response.data;
};

export const getMiner = async (id: string): Promise<Miner> => {
    const response = await api.get(`/miners/${id}`);
    return response.data;
}

export const createMiner = async (miner: Miner): Promise<Miner> => {
    const response = await api.post('/miners', miner);
    return response.data;
}

export const updateMiner = async (miner: Miner): Promise<Miner> => {
    const response = await api.put(`/miners/${miner.id}`, miner);
    return response.data;
}

export const deleteMiner = async (id: string): Promise<void> => {
    await api.delete(`/miners/${id}`);
}   


