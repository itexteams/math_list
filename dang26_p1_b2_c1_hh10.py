import google.generativeai as genai
from sympy.abc import x, y, z, t
import sys
import os
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFileDialog, QMessageBox
)
from pdf2image import convert_from_path
from math import degrees
import openpyxl
from openpyxl import Workbook
from openpyxl.styles import Alignment, Font
from openpyxl.utils import get_column_letter
from sympy import simplify, collect
from itertools import combinations
import itertools
from PyQt5.QtCore import QSettings
import sys
import os
import platform
import subprocess
import hashlib
import time
from datetime import datetime, timedelta
# Bổ sung các widget và core cho Splash Screen
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QDialog, QLabel, QLineEdit, 
    QPushButton, QComboBox, QCheckBox, QTextEdit, QVBoxLayout, 
    QHBoxLayout, QGridLayout, QMessageBox, QColorDialog,
    QSplashScreen, QProgressBar  # <-- BỔ SUNG 2 CÁI NÀY
)
from PyQt5.QtCore import Qt, QSettings, QThread, pyqtSignal  # <-- BỔ SUNG QThread, pyqtSignal
from PyQt5.QtGui import QIcon, QPixmap, QFont
from PyQt5.QtGui import QFont, QBrush, QColor
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QSplitter, QTreeWidget, QTreeWidgetItem, QTextEdit, QLabel, 
    QSpacerItem, QSizePolicy, QStackedWidget, QPushButton, QCheckBox, QSpinBox,
    QScrollArea  # <-- Thêm mục này vào đây
)
from PyQt5.QtWidgets import QCheckBox
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt, QPropertyAnimation, pyqtProperty
from functools import wraps
import re
import uuid
import json, base64
from datetime import datetime
from nacl.signing import VerifyKey
from nacl.encoding import HexEncoder
from nacl.exceptions import BadSignatureError
### CÔNG CỤ
import sys
import numpy as np
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QPushButton, QDialog, 
    QVBoxLayout, QHBoxLayout, QTabWidget, QWidget, 
    QLabel, QSlider, QDoubleSpinBox, QGroupBox
)
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D  # Cần cho 3D


def bt_dang26_p1_b2_c1_hh10(self):
                # Khai báo biến
                # Khai báo biến
                lisdang=['1']
                dang=random.choice(lisdang)
                
                if dang=='1':
                    # B3 - Logic Random bài toán: 
                    # Lặp để chọn ngẫu nhiên 3 cạnh tạo thành một tam giác hợp lệ
                    while True:
                        AB = round(random.uniform(3.0, 8.0), 1)
                        BC = round(random.uniform(3.0, 8.0), 1)
                        CA = round(random.uniform(3.0, 8.0), 1)
                        # Điều kiện để 3 cạnh tạo thành tam giác (có cộng thêm 0.5 để tránh tam giác quá dẹt)
                        if AB + BC > CA + 0.5 and BC + CA > AB + 0.5 and CA + AB > BC + 0.5:
                            break
                            
                    # Chuyển số thập phân sang dạng chuỗi có dấu phẩy kiểu Việt Nam
                    AB_str = str(AB).replace('.', ',')
                    BC_str = str(BC).replace('.', ',')
                    CA_str = str(CA).replace('.', ',')
                
                    # Tính nửa chu vi p
                    p_val = (AB + BC + CA) / 2.0
                    
                    # Xử lý hiển thị p dưới dạng phân số tối giản (giống 31/4 trong bài mẫu)
                    tu_so = int(round((AB + BC + CA) * 10))
                    mau_so = 20
                    ucln = math.gcd(tu_so, mau_so)
                    tu_so = tu_so // ucln
                    mau_so = mau_so // ucln
                    if mau_so == 1:
                        p_str = f"{tu_so}"
                    else:
                        p_str = f"\\frac{{{tu_so}}}{{{mau_so}}}"
                
                    # Tính S bằng công thức Heron và tính R
                    S_val = math.sqrt(p_val * (p_val - AB) * (p_val - BC) * (p_val - CA))
                    R_val = (AB * BC * CA) / (4 * S_val)
                
                    # Làm tròn giống bài mẫu
                    S_round = round(S_val, 1)
                    R_round = round(R_val, 2)
                
                    # Đổi dấu chấm thành phẩy
                    S_str = str(S_round).replace('.', ',')
                    R_str = str(R_round).replace('.', ',')
                
                    # Câu hỏi
                    noidungcauhoi = ('''\\immini{Trong khi khai quật một ngôi mộ cổ, các nhà khảo cổ học đã tìm được một chiếc đĩa cổ hình tròn bị vỡ, các nhà khảo cổ muốn khôi phục lại hình dạng chiếc đĩa này. Để xác định bán kính của chiếc đĩa, các nhà khảo cổ lấy $3$ điểm trên chiếc đĩa và tiến hành đo đạc thu được kết quả như hình vẽ ($AB = %s \\text{ cm}; BC = %s \\text{ cm}; CA = %s \\text{ cm}$). Bán kính chiếc đĩa (Kết quả làm tròn đến hàng phần trăm) bằng}
                    {\\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-0.8,xscale=0.8]
	\\draw  [dash pattern={on 5.63pt off 4.5pt}][line width=1]  (154.1,151.65) .. controls (154.1,99.04) and (196.74,56.4) .. (249.35,56.4) .. controls (301.96,56.4) and (344.6,99.04) .. (344.6,151.65) .. controls (344.6,204.26) and (301.96,246.9) .. (249.35,246.9) .. controls (196.74,246.9) and (154.1,204.26) .. (154.1,151.65) -- cycle ;
	\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.66 ][fill={rgb, 255:red, 186; green, 160; blue, 138 }  ,fill opacity=1 ] (246.6,55.9) -- (250.6,67.4) -- (246.1,71.9) -- (246.6,78.9) -- (249.6,88.4) -- (245.6,97.9) -- (238.6,97.4) -- (227.6,97.9) -- (219.6,87.9) -- (216.1,77.9) -- (213.6,68.9) -- (216.6,62.9) -- (223.6,59.9) -- (235.6,57.9) -- cycle ;
	\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.66 ][fill={rgb, 255:red, 186; green, 160; blue, 138 }  ,fill opacity=1 ] (211.1,65.4) -- (216.1,77.9) -- (217.6,85.9) -- (222.1,93.9) -- (227.6,97.9) -- (222.6,113.9) -- (212.6,122.4) -- (204.6,134.4) -- (195.6,132.9) -- (187.6,131.9) -- (180.1,128.4) -- (173.6,123.4) -- (169.1,118.4) -- (169.1,112.4) -- (164.6,108.9) -- (170.6,97.9) -- (178.1,87.9) -- (183.1,81.9) -- (188.6,77.9) -- (194.6,73.4) -- (202.1,68.4) -- cycle ;
	\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.66 ][fill={rgb, 255:red, 186; green, 160; blue, 138 }  ,fill opacity=1 ] (161.1,118.4) -- (169.6,121.4) -- (180.1,128.4) -- (187.6,131.9) -- (204.6,134.4) -- (205.6,141.9) -- (192.6,152.9) -- (187.6,165.4) -- (181.6,171.4) -- (179.1,176.4) -- (171.1,177.9) -- (166.1,178.4) -- (163.6,182.4) -- (159.6,179.4) -- (156.1,169.9) -- (154.1,159.4) -- (153.6,148.4) -- (154.6,137.4) -- (157.1,126.4) -- cycle ;
	\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.66 ][fill={rgb, 255:red, 186; green, 160; blue, 138 }  ,fill opacity=1 ] (201.1,177.4) -- (191.1,181.4) -- (181.6,181.9) -- (178.6,177.4) -- (181.6,171.4) -- (187.6,165.4) -- (194.1,166.9) -- cycle ;
	\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.66 ][fill={rgb, 255:red, 186; green, 160; blue, 138 }  ,fill opacity=1 ] (191.1,181.4) -- (201.1,177.4) -- (211.6,185.9) -- (215.1,191.9) -- (220.1,202.9) -- (222.1,211.4) -- (227.1,215.9) -- (233.6,219.9) -- (226.1,222.9) -- (220.1,227.9) -- (217.6,240.9) -- (205.6,237.4) -- (196.6,231.9) -- (185.6,223.9) -- (178.1,215.9) -- (171.1,206.4) -- (167.1,200.4) -- (163.1,192.9) -- (166.1,186.9) -- (175.1,182.9) -- (179.6,181.9) -- cycle ;
	\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.66 ][fill={rgb, 255:red, 186; green, 160; blue, 138 }  ,fill opacity=1 ] (241.1,207.4) -- (241.1,212.4) -- (236.6,217.4) -- (233.6,219.9) -- (227.1,215.9) -- (222.1,211.4) -- (220.1,202.9) -- (226.6,204.4) -- cycle ;
	\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.66 ][fill={rgb, 255:red, 186; green, 160; blue, 138 }  ,fill opacity=1 ] (240.1,227.9) -- (246.6,233.9) -- (249.35,246.9) -- (241.6,245.4) -- (231.6,244.9) -- (221.6,241.9) -- (220.1,227.9) -- (226.1,222.9) -- (233.6,219.9) -- (240.1,221.4) -- cycle ;
	\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.66 ][fill={rgb, 255:red, 186; green, 160; blue, 138 }  ,fill opacity=1 ] (269.1,218.9) -- (272.1,223.9) -- (256.6,235.9) -- (249.1,242.4) -- (247.1,234.4) -- (242.1,229.9) -- (240.1,221.4) -- (241.1,212.4) -- (245.6,206.9) -- (253.6,208.9) -- (259.6,214.4) -- cycle ;
	\\draw  [color={rgb, 255:red, 0; green, 0; blue, 0 }  ,draw opacity=0.66 ][fill={rgb, 255:red, 186; green, 160; blue, 138 }  ,fill opacity=1 ] (321.6,196.4) -- (331.6,199.4) -- (325.1,209.9) -- (317.6,217.9) -- (307.6,227.4) -- (298.1,233.9) -- (289.6,227.9) -- (282.1,223.9) -- (272.1,223.9) -- (269.1,218.9) -- (271.6,202.9) -- (283.6,195.4) -- (292.6,185.4) -- (303.1,188.4) -- (308.1,188.4) -- (313.6,191.9) -- cycle ;
	\\draw [color={rgb, 255:red, 139; green, 87; blue, 42 }  ,draw opacity=1 ]   (169.1,118.4) .. controls (183.6,82.4) and (227.1,65.9) .. (250.6,67.4) ;
	\\draw [color={rgb, 255:red, 139; green, 87; blue, 42 }  ,draw opacity=1 ]   (168.6,175.9) .. controls (163.1,165.4) and (157.6,143.4) .. (169.6,121.4) ;
	\\draw [color={rgb, 255:red, 139; green, 87; blue, 42 }  ,draw opacity=1 ]   (219.6,235.9) .. controls (200.6,224.9) and (173.6,204.9) .. (170.6,184.9) ;
	\\draw [color={rgb, 255:red, 139; green, 87; blue, 42 }  ,draw opacity=1 ]   (246.6,239.9) .. controls (237.6,239.4) and (231.6,237.9) .. (222.1,234.9) ;
	\\draw [color={rgb, 255:red, 139; green, 87; blue, 42 }  ,draw opacity=1 ]   (321.1,197.4) .. controls (314.1,209.9) and (303.6,219.9) .. (291.6,226.9) ;
	\\draw [color={rgb, 255:red, 139; green, 87; blue, 42 }  ,draw opacity=1 ]   (187.6,131.9) .. controls (197.6,100.4) and (229.6,89.9) .. (249.1,85.9) ;
	\\draw [color={rgb, 255:red, 139; green, 87; blue, 42 }  ,draw opacity=1 ]   (187.6,165.4) .. controls (185.1,153.9) and (185.1,142.9) .. (187.6,131.9) ;
	\\draw [color={rgb, 255:red, 139; green, 87; blue, 42 }  ,draw opacity=1 ]   (241.1,212.4) .. controls (220.6,204.9) and (190.6,186.4) .. (187.6,166.4) ;
	\\draw [color={rgb, 255:red, 139; green, 87; blue, 42 }  ,draw opacity=1 ]   (300.1,187.9) .. controls (293.1,200.4) and (283.1,206.9) .. (271.1,213.9) ;
	\\draw [color={rgb, 255:red, 139; green, 87; blue, 42 }  ,draw opacity=1 ]   (188.6,157.9) .. controls (183.6,111.9) and (228.1,91.4) .. (249.6,88.4) ;
	\\draw [color={rgb, 255:red, 139; green, 87; blue, 42 }  ,draw opacity=1 ]   (217.1,196.4) .. controls (203.1,183.9) and (194.1,185.4) .. (191.1,165.4) ;
	\\draw [color={rgb, 255:red, 139; green, 87; blue, 42 }  ,draw opacity=1 ]   (297.1,186.4) .. controls (290.1,198.9) and (283.1,203.9) .. (271.1,210.9) ;
	\\draw [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ][line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (249.35,151.65) -- (320.1,213.9) ;
	\\draw [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ][line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (249.35,151.65) -- (156.1,169.9) ;
	\\draw [color={rgb, 255:red, 208; green, 2; blue, 27 }  ,draw opacity=1 ][line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (249.35,151.65) -- (241.6,56.9) ;
	\\draw [color={rgb, 255:red, 20; green, 66; blue, 120 }  ,draw opacity=1 ][line width=1]    (156.1,169.9) -- (241.6,56.9) ;
	\\draw [color={rgb, 255:red, 20; green, 66; blue, 120 }  ,draw opacity=1 ][line width=1]    (320.1,213.9) -- (241.6,56.9) ;
	\\draw [color={rgb, 255:red, 20; green, 66; blue, 120 }  ,draw opacity=1 ][line width=1]    (156.1,169.9) -- (320.1,213.9) ;
	\\draw (135,159) node [anchor=north west][inner sep=0.75pt]    {$A$};
	\\draw (233,33.5) node [anchor=north west][inner sep=0.75pt]    {$B$};
	\\draw (321,209) node [anchor=north west][inner sep=0.75pt]    {$C$};
	\\draw (235.5,152.5) node [anchor=north west][inner sep=0.75pt]    {$O$};
	\\draw (228,110.5) node [anchor=north west][inner sep=0.75pt]    {$R$};
\\end{tikzpicture}}'''
                                     %(AB_str, BC_str, CA_str))
                
                    # Tạo các đáp án gây nhiễu
                    wrong_answers = set()
                    while len(wrong_answers) < 3:
                        # Tạo số ngẫu nhiên dao động quanh kết quả đúng
                        w = round(R_val + random.uniform(-1.5, 1.5), 2)
                        if w != R_round and w > 0:
                            wrong_answers.add(w)
                            
                    wrong_answers = list(wrong_answers)
                
                    # Định dạng LaTeX cho các đáp án
                    da_d = ('\\True $%s\\,cm$' % R_str)
                    da_s1 = ('$%s\\,cm$' % str(wrong_answers[0]).replace('.', ','))
                    da_s2 = ('$%s\\,cm$' % str(wrong_answers[1]).replace('.', ','))
                    da_s3 = ('$%s\\,cm$' % str(wrong_answers[2]).replace('.', ','))
                
                    # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                    list_1 = [da_d, da_s1, da_s2, da_s3]
                    random.shuffle(list_1)
                
                    # Nội dung lời giải
                    loigiai = ('''Bán kính $R$ của chiếc đĩa bằng bán kính đường tròn ngoại tiếp tam giác $ABC$.\\\\
                Nửa chu vi của tam giác $ABC$ là: $p = \\frac{AB + BC + CA}{2} = \\frac{%s + %s + %s}{2} = %s\\,cm$.\\\\
                Diện tích tam giác $ABC$ là: $S = \\sqrt{p(p - AB)(p - BC)(p - CA)} \\approx %s\\,cm^2$.\\\\
                Mà $S = \\frac{AB.BC.CA}{4R} \\Rightarrow R = \\frac{AB.BC.CA}{4S} \\approx %s\\,cm$.'''
                               %(AB_str, BC_str, CA_str, p_str, S_str, R_str))
                
                # Xử lý chuỗi hiển thị tránh lỗi dấu + - hoặc - - theo lưu ý
                noidungcauhoi = noidungcauhoi.replace('+ -', '-').replace('- -', '+')
                loigiai = loigiai.replace('+ -', '-').replace('- -', '+')
                
                # Xuất câu trắc nghiệm
                content = ('\\begin{minipage}{\\textwidth} \n'
                    '\\begin{ex}\n'+ str(noidungcauhoi)+ '\n'
                    '\\choice \n'
                    '{'+str(list_1[1])+'}\n'
                    '{'+str(list_1[2])+'}\n'
                    '{'+str(list_1[3])+'}\n'
                    '{'+str(list_1[0])+'}\n'
                    '\\loigiai{'+str(loigiai)+'}\n'
                    '\\end{ex}\n\\end{minipage} \n\n')
                return content