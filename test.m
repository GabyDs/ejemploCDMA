%% Ejemplo CDMA

clc
clear all
close all


% Parametros

n_data = 3;     % nro bits de datos
n_PN = 30;       % nro de bits secuencia pseudo aleatoria
n = 2;          % cantidad de usuarios simultaneos

%% Generacion de datos

% generacion de datos y las secuencias pseudo aleatorias para la
% codificacion
data = randi([0 1],n_data,n);
PN = randi([0 1],n_PN,n);

PN

for i = 1:n;
    disp(strcat("Data usuario ",i))
    transpose(data(:,i))
end
for i = 1:n;
    disp(strcat("Secuencia pseudoaleatoria usuario ",i))
    transpose(PN(:,i))
end
%% Codificacion
%
% codificacion
data = 2*data-1;

for i = 1:n
    signal(:,i) = kron(data(:,i),PN(:,i));
end
signal
%%
% concatena la secuencia PN n_data veces
PN_long = repmat(PN,[n_data 1]);

PN_long

% repite los datos para graficar
PN_mat_plot = repelem(PN_long,100,1);
data_plot = repelem(data,100,1);
signal_plot = repelem(signal,100,1);

L=length(data_plot);

figure
subplot(3,1,1)
plot(data_plot(:,1),'linewidth',3)
title('data')
% configs grafico
set(gca,'XTick',0:data_plot*100:L);
set(gca,'XTickLabel',0:n_data);

