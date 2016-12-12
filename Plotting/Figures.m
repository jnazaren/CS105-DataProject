

%%%%%   Plotting Death Toll and Damage based on Richter Scale on World Map

load('Earthquake_data.mat')

% Sets specific colors

cmap = jet((max(ed(:,1) * 10)));

% Plots world map with coastlines
worldmap world
load coastlines
[latcells, loncells] = polysplit(coastlat, coastlon);

% Death Based on Richter Value

figure(1)
title('Death Based on Richter Scale') 
plotm(coastlat,coastlon)
set(gcf, 'units','normalized','outerposition',[0 0 1 1])
colormap('jet')
hold on;
c = colorbar('Location','SouthOutside','Ticks',[0 .11 .22 .33 .44 .55 .66 .77 .88 1],...
    'TickLabels',{'0','1','2','3','4','5','6','7','8','9'});
c.Label.String = 'Richter Scale';

% Creates Size Legend

h(1) = plotm(0,0,'o','MarkerSize',6,'MarkerFaceColor','c');
h(2) = plotm(0,0,'o','MarkerSize',8,'MarkerFaceColor','c');
h(3) = plotm(0,0,'o','MarkerSize',10,'MarkerFaceColor','c');
h(4) = plotm(0,0,'o','MarkerSize',12,'MarkerFaceColor','c');
h(5) = plotm(0,0,'o','MarkerSize',14,'MarkerFaceColor','c');
hLegend = legend(h,'None','1 to 50','51 to 100','101 to 1000','> 1001','Location','SouthEastOutside');
hLegendAxes = axes('Parent',hLegend.Parent, 'Units',hLegend.Units, 'Position',hLegend.Position, ...
                   'XTick',[] ,'YTick',[], 'Color','none', 'YColor','none', 'XColor','none', 'HandleVisibility','off', 'HitTest','off');
% Add the axes title (will appear directly above the legend box)
title(hLegendAxes, 'Number of Deaths', 'FontWeight','bold', 'FontSize',8);  % Default is bold-11, which is too large

% delete(h(1))
% delete(h(2))
% delete(h(3))
% delete(h(4))
% delete(h(5))

for ii = 1: length(ed)
    figure(1);
    if ed(ii,5) == 0
        hold on
        plotm(ed(ii,2),ed(ii,3),'o','MarkerSize',6,'MarkerFaceColor',cmap((ed(ii,1)*10),:))
    end
    if ed(ii,5) == 1
        hold on
        plotm(ed(ii,2),ed(ii,3),'o','MarkerSize',8,'MarkerFaceColor',cmap((ed(ii,1)*10),:))
    end
    if ed(ii,5) == 2
        hold on
        plotm(ed(ii,2),ed(ii,3),'o','MarkerSize',10,'MarkerFaceColor',cmap((ed(ii,1)*10),:))
    end
    if ed(ii,5) == 3
        hold on
        plotm(ed(ii,2),ed(ii,3),'o','MarkerSize',12,'MarkerFaceColor',cmap((ed(ii,1)*10),:))
    end
    if ed(ii,5) == 4
        hold on
        plotm(ed(ii,2),ed(ii,3),'o','MarkerSize',14,'MarkerFaceColor',cmap((ed(ii,1)*10),:))
    end
end
% Damage Based on Richter Value

figure(2)
worldmap world
load coastlines
plotm(coastlat,coastlon)
set(gcf, 'units','normalized','outerposition',[0 0 1 1])
title('Damage Based on Richter Scale')
colormap('jet')
hold on;
c = colorbar('Location','SouthOutside','Ticks',[0 .11 .22 .33 .44 .55 .66 .77 .88 1],...
    'TickLabels',{'0','1','2','3','4','5','6','7','8','9'});
c.Label.String = 'Richter Scale';

% Creates Size Legend

h(1) = plotm(0,0,'o','MarkerSize',6,'MarkerFaceColor','c');
h(2) = plotm(0,0,'o','MarkerSize',8,'MarkerFaceColor','c');
h(3) = plotm(0,0,'o','MarkerSize',10,'MarkerFaceColor','c');
h(4) = plotm(0,0,'o','MarkerSize',12,'MarkerFaceColor','c');
h(5) = plotm(0,0,'o','MarkerSize',14,'MarkerFaceColor','c');
hLegend = legend(h,'None','< 1 Million','1 to 5','5 to 24','> 25 Million','Location','SouthEastOutside');
hLegendAxes = axes('Parent',hLegend.Parent, 'Units',hLegend.Units, 'Position',hLegend.Position, ...
                   'XTick',[] ,'YTick',[], 'Color','none', 'YColor','none', 'XColor','none', 'HandleVisibility','off', 'HitTest','off');
% Add the axes title (will appear directly above the legend box)
hTitle = title(hLegendAxes, 'Amount of Damage (Millions)', 'FontWeight','bold', 'FontSize',8);  % Default is bold-11, which is too large

% figure(1)
% delete(h(1))
% delete(h(2))
% delete(h(3))
% delete(h(4))
% delete(h(5))
% 
for ii = 1: length(ed)
      figure(2);
    if ed(ii,4) == 1
        plotm(ed(ii,2),ed(ii,3),'o','MarkerSize',6,'MarkerFaceColor',cmap((ed(ii,1)*10),:))
    end
    if ed(ii,4) == 2
       plotm(ed(ii,2),ed(ii,3),'o','MarkerSize',7,'MarkerFaceColor',cmap((ed(ii,1)*10),:))
    end
    if ed(ii,4) == 3
        plotm(ed(ii,2),ed(ii,3),'o','MarkerSize',8,'MarkerFaceColor',cmap((ed(ii,1)*10),:))
    end
    if ed(ii,4) == 4
        plotm(ed(ii,2),ed(ii,3),'o','MarkerSize',9,'MarkerFaceColor',cmap((ed(ii,1)*10),:))
    end
    if ed(ii,4) == 5
        plotm(ed(ii,2),ed(ii,3),'o','MarkerSize',10,'MarkerFaceColor',cmap((ed(ii,1)*10),:))
    end  
    
end



