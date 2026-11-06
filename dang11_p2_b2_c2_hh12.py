import sys
from PyQt5.QtWidgets import QApplication, QColorDialog, QMainWindow, QSplitter, QTreeWidget, QSpacerItem, QSizePolicy, QTreeWidgetItem, QCheckBox, QFileDialog, QVBoxLayout, QTextEdit, QPushButton, QWidget, QLabel, QLineEdit, QDialog, QAction, QMessageBox, QScrollBar, QHeaderView, QMenu, QGridLayout
from sympy import *
from sympy.abc import x
import sympy as sp
from sympy import symbols,sqrt,evaluate,Subs,latex, Rational, expand, simplify, integrate
import random
import math
from sympy import Rational
from fractions import Fraction as frac
from random import randint
from PyQt5.QtGui import QTextCursor
from PyQt5.QtGui import QFont
import hashlib
import uuid
import os
from sympy import symbols, Eq, solve
import numpy as np
from PyQt5.QtGui import QIcon
from math import factorial
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QTextDocument
from subprocess import run, CalledProcessError
import shutil
from PyQt5.QtWidgets import QProgressBar
from docx import Document
from PyQt5 import QtGui
import re
import pandas as pd
from PyQt5.QtGui import QPixmap
import subprocess
import platform
import json
from decimal import Decimal, ROUND_HALF_UP
from PyQt5.QtWidgets import QComboBox, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QSpinBox, QTreeWidget, QTreeWidgetItem, QCheckBox, QTextEdit, QPushButton, QHBoxLayout
from random import randint, choice, shuffle
from sympy import latex
from fractions import Fraction
from collections import Counter
from random import sample
import shutil
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt
import qrcode
import json
import glob
import os
import platform
import subprocess
import hashlib
import base64
from datetime import datetime, timedelta
from PyQt5.QtWidgets import (QApplication, QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox)
from sympy import symbols, solve, Lt
#from PyQt5.QtWebEngineWidgets import QWebEngineView
#from PyQt5.QtCore import QUrl
#from sympy import latex
import re
import pyperclip
import warnings
warnings.filterwarnings("ignore", category=FutureWarning)

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


def bt_dang11_p2_b2_c2_hh12(self):
            # Khai báo biến
            # Khai báo biến
            # random v_max
            v_max = random.choice([40, 50, 60])
            z_S = random.choice([14, 15, 16])
            SA_val = random.choice([25, 27, 29])
            OD_val = random.choice([6, 7, 8])
            AB_val = random.choice([12, 14, 16])
            CD_val = random.choice([8.6, 9.6, 10.6])
            v_oto = random.choice([45, 50, 55])
            y_M = random.choice([-5, -6, -7])
            t_time = random.choice([0.6, 0.7, 0.8])

            # Các tính toán
            DH = CD_val / 2
            y_D = -DH
            x_D = math.sqrt(OD_val**2 - DH**2)
            x_D_str = str(round(x_D, 2)).replace('.', ',')

            AK = AB_val / 2
            y_A = -AK
            # Sửa lại công thức tính x_A:
            OA_val = math.sqrt(SA_val**2 - z_S**2)
            x_A = math.sqrt(OA_val**2 - y_A**2)  # hoặc: math.sqrt(SA_val**2 - z_S**2 - y_A**2)
            x_A_str = str(round(x_A, 2)).replace(".", ",")

            DA_vec_x = x_A - x_D
            DA_vec_y = y_A - y_D
            DA_vec_x_str = str(round(DA_vec_x, 2)).replace('.', ',')
            DA_vec_y_str = str(round(DA_vec_y, 2)).replace('.', ',')

            # Biến đã được làm tròn để hiển thị chính xác trong phương trình (ý b)
            abs_DA_vec_y_str = str(round(abs(DA_vec_y), 2)).replace('.', ',')

            MF = 50 - x_A
            t_MF = MF / (v_oto / 3.6)
            t_MF_str = str(round(t_MF, 2)).replace('.', ',')

            EF_val = (DA_vec_x) * abs(y_M - y_A) / abs(y_D - y_A)
            v_real = (EF_val / t_time) * 3.6

            EF_str = str(round(EF_val, 2)).replace('.', ',')
            v_real_str = str(round(v_real, 2)).replace('.', ',')
            hinhve=r'''\scalebox{0.8}{ \begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
            	\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (280,166.8) -- (280,25.47) ;
            	\draw [shift={(280,21.47)}, rotate = 90] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (15.6,-3.9) -- (0,0) -- (15.6,3.9) -- cycle    ;
            	\draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (106.4,64.54) -- (276.4,64.54) -- (276.4,67.33) -- (106.4,67.33) -- cycle ;
            	\draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (171.88,64.28) .. controls (171.88,60.79) and (174.71,57.97) .. (178.19,57.97) -- (211.09,57.97) .. controls (214.58,57.97) and (217.4,60.79) .. (217.4,64.28) -- (217.4,65.83) .. controls (217.4,69.31) and (214.58,72.13) .. (211.09,72.13) -- (178.19,72.13) .. controls (174.71,72.13) and (171.88,69.31) .. (171.88,65.83) -- cycle ;
            	\draw  [fill={rgb, 255:red, 251; green, 3; blue, 31 }  ,fill opacity=1 ] (202.25,65.25) .. controls (202.25,62.42) and (204.54,60.13) .. (207.37,60.13) .. controls (210.19,60.13) and (212.48,62.42) .. (212.48,65.25) .. controls (212.48,68.08) and (210.19,70.37) .. (207.37,70.37) .. controls (204.54,70.37) and (202.25,68.08) .. (202.25,65.25) -- cycle ;
            	\draw  [fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ] (189.52,65.25) .. controls (189.52,62.42) and (191.81,60.13) .. (194.64,60.13) .. controls (197.47,60.13) and (199.76,62.42) .. (199.76,65.25) .. controls (199.76,68.08) and (197.47,70.37) .. (194.64,70.37) .. controls (191.81,70.37) and (189.52,68.08) .. (189.52,65.25) -- cycle ;
            	\draw  [fill={rgb, 255:red, 126; green, 211; blue, 33 }  ,fill opacity=1 ] (176.08,65.25) .. controls (176.08,62.42) and (178.37,60.13) .. (181.2,60.13) .. controls (184.03,60.13) and (186.32,62.42) .. (186.32,65.25) .. controls (186.32,68.08) and (184.03,70.37) .. (181.2,70.37) .. controls (178.37,70.37) and (176.08,68.08) .. (176.08,65.25) -- cycle ;
            	\draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (256.34,53.05) .. controls (267.54,52.54) and (268.32,53.33) .. (271.07,56.85) .. controls (262.45,65.47) and (266.37,65.47) .. (254.22,74.87) .. controls (242.47,75.26) and (238.16,74.87) .. (237.77,67.43) .. controls (236.61,65.95) and (233.63,67) .. (233.07,64.29) .. controls (239.33,59.59) and (245.99,58.03) .. (256.34,53.05) -- cycle ;
            	\draw  [fill={rgb, 255:red, 248; green, 231; blue, 28 }  ,fill opacity=1 ] (241.06,69.19) .. controls (241.06,67.79) and (242.2,66.65) .. (243.6,66.65) -- (248.54,66.65) .. controls (249.95,66.65) and (251.09,67.79) .. (251.09,69.19) -- (251.09,69.19) .. controls (251.09,70.6) and (249.95,71.74) .. (248.54,71.74) -- (243.6,71.74) .. controls (242.2,71.74) and (241.06,70.6) .. (241.06,69.19) -- cycle ;
            	\draw    (257.9,68.33) -- (265.19,62.34) ;
            	\draw    (237.77,65.47) -- (253.83,65.47) ;
            	\draw  [fill={rgb, 255:red, 74; green, 74; blue, 74 }  ,fill opacity=1 ] (113.4,55.67) -- (120.33,55.67) -- (120.33,166.13) -- (113.4,166.13) -- cycle ;
            	\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (119.73,166.13) -- (393.73,166.13) ;
            	\draw  [fill={rgb, 255:red, 80; green, 227; blue, 194 }  ,fill opacity=1 ] (330.2,181.13) -- (379.73,232.8) -- (151.07,232.13) -- (220.4,181.47) -- cycle ;
            	\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (220.4,181.47) -- (280.3,65.33) ;
            	\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (330.2,181.13) -- (280.3,69.23) ;
            	\draw [line width=1]    (151.07,232.13) -- (280.3,69.23) ;
            	\draw [line width=1]    (379.73,232.8) -- (280.3,69.23) ;
            	\draw  [fill={rgb, 255:red, 80; green, 227; blue, 194 }  ,fill opacity=1 ] (276.4,66.33) .. controls (276.4,64.18) and (278.15,62.43) .. (280.3,62.43) .. controls (282.45,62.43) and (284.2,64.18) .. (284.2,66.33) .. controls (284.2,68.49) and (282.45,70.23) .. (280.3,70.23) .. controls (278.15,70.23) and (276.4,68.49) .. (276.4,66.33) -- cycle ;
            	\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (280,166.8) -- (242.53,261.75) ;
            	\draw [shift={(241.07,265.47)}, rotate = 291.53] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (15.6,-3.9) -- (0,0) -- (15.6,3.9) -- cycle    ;
            	\draw (262,22) node [anchor=north west][inner sep=0.75pt]    {$z$};
            	\draw (286,56.33) node [anchor=north west][inner sep=0.75pt]    {$S$};
            	\draw (260,148) node [anchor=north west][inner sep=0.75pt]    {$O$};
            	\draw (132,218) node [anchor=north west][inner sep=0.75pt]    {$A$};
            	\draw (382.67,218.33) node [anchor=north west][inner sep=0.75pt]    {$B$};
            	\draw (316,182) node [anchor=north west][inner sep=0.75pt]    {$C$};
            	\draw (216,182) node [anchor=north west][inner sep=0.75pt]    {$D$};
            	\draw (230,244) node [anchor=north west][inner sep=0.75pt]    {$x$};
            \end{tikzpicture} }'''
            # Nội dung câu hỏi
            noidungcauhoi = (r'''\immini{Tại một nút giao thông của một khu vực đông dân cư với tốc độ tối đa cho phép đối với ô tô là $%s$ (km/h), người ta gắn một camera phạt nguội tại điểm $S(0;0;%s)$ trong không gian $Oxyz$ (đơn vị trên mỗi trục tọa độ là mét), mặt phẳng $Oxy$ song song với mặt đường và chứa vùng nhận diện biển số xe của các phương tiện tham gia giao thông. Biết rằng camera nhận diện tốt nhất biển số xe của các phương tiện tham gia giao thông là khi biển số của chúng nằm trong hình thang cân $ABCD$ với: $SA = SB = %s$ mét, $OD = OC = %s$ mét, $AB = %s$ mét và $CD = %s$ mét. Tia $Ox$ nằm trên đường trung trực các đoạn thẳng $AB$ và $DC$ (xem hình vẽ minh họa). Giả sử tại thời điểm $9h00$ (được xem là thời điểm xuất phát) một ô tô chuyển động thẳng đều theo phương song song với trục $Ox$, hướng về phía trục $Oy$ và có vị trí của biển số xe là $M(50;%s;0)$.}{%s}'''
            % (v_max, z_S, SA_val, OD_val, AB_val, str(CD_val).replace('.', ','), y_M, hinhve))

            ######################################################################## Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True $D(%s;%s;0)$' % (x_D_str, str(y_D).replace('.', ','))
            nb_da_1_s_val = str(round(x_D + 1, 2)).replace('.', ',')
            nb_da_1_s = '$D(%s;%s;0)$' % (nb_da_1_s_val, str(y_D).replace('.', ','))
            list_nb_da_1=[nb_da_1_d,nb_da_1_s]
            nb_da_1=random.choice(list_nb_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = ('''Xét $(Oxy)$, gọi $H$ là trung điểm $CD$, ta có $CD = %s \\Rightarrow DH = %s \\Rightarrow y_D = %s$.
                            \\begin{center}
                            	\\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
                            		\\draw [line width=1]    (67,143.53) -- (300.6,145.14) ;
                            		\\draw [shift={(304.6,145.16)}, rotate = 180.39] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (13.4,-6.43) -- (0,0) -- (13.4,6.44) -- (8.9,0) -- cycle    ;
                            		\\draw [line width=1]    (92.79,238.52) -- (93.36,55.22) ;
                            		\\draw [shift={(93.37,51.22)}, rotate = 90.18] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (13.4,-6.43) -- (0,0) -- (13.4,6.44) -- (8.9,0) -- cycle    ;
                            		\\draw [line width=1]    (93.08,144.87) -- (231.66,222.18) ;
                            		\\draw [line width=1]    (231.66,222.18) -- (232.25,64.06) ;
                            		\\draw [line width=1]    (162.23,104.32) -- (232.25,64.06) ;
                            		\\draw [line width=1]    (162.23,104.32) -- (162.37,183.53) ;
                            		\\draw (72.09,149) node [anchor=north west][inner sep=0.75pt]    {$O$};
                            		\\draw (219.88,223.22) node [anchor=north west][inner sep=0.75pt]    {$A$};
                            		\\draw (225.88,44) node [anchor=north west][inner sep=0.75pt]    {$B$};
                            		\\draw (150.11,85) node [anchor=north west][inner sep=0.75pt]    {$C$};
                            		\\draw (151.44,186.21) node [anchor=north west][inner sep=0.75pt]    {$D$};
                            		\\draw (141.52,148) node [anchor=north west][inner sep=0.75pt]    {$H$};
                            		\\draw (233.37,148) node [anchor=north west][inner sep=0.75pt]    {$K$};
                            		\\draw (284.23,149) node [anchor=north west][inner sep=0.75pt]    {$x$};
                            		\\draw (71.84,51) node [anchor=north west][inner sep=0.75pt]    {$y$};
                            	\\end{tikzpicture}
                            \\end{center}
            Tam giác $DOH$ vuông tại $H$ nên $OH = \\sqrt{OD^2 - DH^2} = \\sqrt{%s^2 - %s^2} \\approx %s \\Rightarrow x_D \\approx %s$. \\\\
            Vậy $D(%s;%s;0)$.'''
            % (str(CD_val).replace('.', ','), str(DH).replace('.', ','), str(y_D).replace('.', ','),
               OD_val, str(DH).replace('.', ','), x_D_str, x_D_str,
               x_D_str, str(y_D).replace('.', ',')))

            # Đưa các lời giải vào danh sách lời giải
            list_nb_2 = [loigiai_nb_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_nb = list(zip(list_nb_1, list_nb_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_nb)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ######################################################################## Thông hiểu ############################################
            # Các đáp án
            th_da_1_d = '\\True Đường thẳng $AD$ có phương trình là $\\begin{cases} x = %s - %s t \\\\ y = %s + %s t, (t \\in \\mathbb{R}) \\\\ z = 0 \\end{cases}$' % (x_D_str, DA_vec_x_str, str(y_D).replace('.', ','), abs_DA_vec_y_str)
            th_da_1_s = 'Đường thẳng $AD$ có phương trình là $\\begin{cases} x = %s + %s t \\\\ y = %s + %s t, (t \\in \\mathbb{R}) \\\\ z = 0 \\end{cases}$' % (x_D_str, DA_vec_x_str, str(y_D).replace('.', ','), abs_DA_vec_y_str)
            list_th_da_1=[th_da_1_d,th_da_1_s]
            th_da_1=random.choice(list_th_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1]

            # Nội dung lời giải
            loigiai_th_1 = (
                r"""Do $AB = %s \Rightarrow AK = %s \Rightarrow y_A = %s$. \\
            Ta có tam giác $SOA$ vuông tại $O$ nên:
            $OA = \sqrt{SA^2 - SO^2} = \sqrt{%s^2 - %s^2} = %s$. \\
            Lại có tam giác $OKA$ vuông tại $K$ nên:
            $x_A = OK = \sqrt{OA^2 - AK^2} = \sqrt{%s^2 - %s^2} \approx %s$. \\
            Suy ra $A(%s;%s;0) \Rightarrow \overrightarrow{DA} = (%s;%s;0)$. \\
            Đường thẳng $AD$ đi qua $D(%s;%s;0)$ và nhận $\overrightarrow{u} = \overrightarrow{DA} = (%s;%s;0)$ làm vectơ chỉ phương có phương trình:
            $\begin{cases} x = %s + %s t \\ y = %s + %s t, (t \in \mathbb{R}) \\ z = 0 \end{cases}$."""
                % (
                    AB_val,
                    str(AK).replace(".", ","),
                    str(y_A).replace(".", ","),
                    SA_val,
                    z_S,
                    str(round(OA_val, 2)).replace(".", ","),
                    str(round(OA_val, 2)).replace(".", ","),
                    str(AK).replace(".", ","),
                    x_A_str,
                    x_A_str,
                    str(y_A).replace(".", ","),
                    DA_vec_x_str,
                    DA_vec_y_str,
                    x_D_str,
                    str(y_D).replace(".", ","),
                    DA_vec_x_str,
                    DA_vec_y_str,
                    x_D_str,
                    DA_vec_x_str,
                    str(y_D).replace(".", ","),
                    abs_DA_vec_y_str,
                )
            )

            # Đưa các lời giải vào danh sách lời giải
            list_th_2 = [loigiai_th_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_th = list(zip(list_th_1, list_th_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_th)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ######################################################################## Vận dụng ############################################
            # Các đáp án
            vd_da_1_d = '\\True Nếu ô tô đi với vận tốc $%s$ (km/h) thì sau đúng $%s$ giây kể từ thời điểm xuất phát thì biển số của xe ôtô đã nằm trong vùng nhận diện tốt nhất của camera' % (v_oto, t_MF_str)
            vd_da_1_s = 'Nếu ô tô đi với vận tốc $%s$ (km/h) thì sau đúng $%s$ giây kể từ thời điểm xuất phát thì biển số của xe ôtô đã nằm trong vùng nhận diện tốt nhất của camera' % (v_oto, str(round(t_MF + 1, 2)).replace('.', ','))
            list_vd_da_1=[vd_da_1_d,vd_da_1_s]
            vd_da_1=random.choice(list_vd_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            loigiai_vd_1 = ('''Biển số của xe ôtô đã nằm trong vùng nhận diện tốt nhất của camera khi ô tô đi qua hình thang cân $ABCD$ tạo hai giao điểm $E, F$ như hình vẽ.
                            \\begin{center}
                            	\\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
                            		\\draw [line width=1]    (67,143.53) -- (451.73,143.53) ;
                            		\\draw [shift={(455.73,143.53)}, rotate = 180] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (13.4,-6.43) -- (0,0) -- (13.4,6.44) -- (8.9,0) -- cycle    ;
                            		\\draw [line width=1]    (92.79,238.52) -- (93.36,55.22) ;
                            		\\draw [shift={(93.37,51.22)}, rotate = 90.18] [fill={rgb, 255:red, 0; green, 0; blue, 0 }  ][line width=0.08]  [draw opacity=0] (13.4,-6.43) -- (0,0) -- (13.4,6.44) -- (8.9,0) -- cycle    ;
                            		\\draw [line width=1]    (93.08,144.87) -- (231.66,222.18) ;
                            		\\draw [line width=1]    (231.66,222.18) -- (232.25,64.06) ;
                            		\\draw [line width=1]    (162.23,104.32) -- (232.25,64.06) ;
                            		\\draw [line width=1]    (162.23,104.32) -- (162.37,183.53) ;
                            		\\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (91.73,183.47) -- (232.4,183.47) ;
                            		\\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (91,222.18) -- (231.66,222.18) ;
                            		\\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (93.73,200.13) -- (402.4,200.13) ;
                            		\\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (402.4,200.13) -- (402.4,143.47) ;
                            		\\draw (72.09,147.45) node [anchor=north west][inner sep=0.75pt]    {$O$};
                            		\\draw (219.88,223.22) node [anchor=north west][inner sep=0.75pt]    {$A$};
                            		\\draw (225.88,43.17) node [anchor=north west][inner sep=0.75pt]    {$B$};
                            		\\draw (150.11,82.26) node [anchor=north west][inner sep=0.75pt]    {$C$};
                            		\\draw (162.11,162.21) node [anchor=north west][inner sep=0.75pt]    {$D$};
                            		\\draw (142.19,121.62) node [anchor=north west][inner sep=0.75pt]    {$H$};
                            		\\draw (233.37,144.96) node [anchor=north west][inner sep=0.75pt]    {$K$};
                            		\\draw (440.9,152) node [anchor=north west][inner sep=0.75pt]    {$x$};
                            		\\draw (71.84,48.17) node [anchor=north west][inner sep=0.75pt]    {$y$};
                            		\\draw (232.75,169.45) node [anchor=north west][inner sep=0.75pt]    {$I$};
                            		\\draw (232.09,202) node [anchor=north west][inner sep=0.75pt]    {$F$};
                            		\\draw (402.4,200.13) node [anchor=north west][inner sep=0.75pt]    {$M$};
                            	\\end{tikzpicture}
                            \\end{center}
            Ta có: $MF = 50 - %s = %s$ mét. \\\\
            Thời gian từ $M$ đến $F$ là $t_{M \\rightarrow F} = \\frac{MF}{v_{ô tô}} = \\frac{%s}{\\frac{%s}{3,6}} = %s$ (giây).'''
            % (str(round(x_A, 2)).replace('.', ','), str(round(MF, 2)).replace('.', ','),
               str(round(MF, 2)).replace('.', ','), v_oto, t_MF_str))

            # Đưa các lời giải vào danh sách lời giải
            list_vd_2 = [loigiai_vd_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_vd = list(zip(list_vd_1, list_vd_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_vd)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ######################################################################## Vận dụng cao ############################################
            # Các đáp án
            vdc_da_1_d = '\\True Nếu camera ghi nhận được hình ảnh biển số xe ô tô liên tục trong một khoảng thời gian kéo dài đúng $%s$ giây, và khoảng thời gian $%s$ giây này kết thúc đồng thời với thời điểm xe vừa ra khỏi vùng nhận diện tốt nhất, thì ôtô đã vượt quá tốc độ cho phép' % (str(t_time).replace('.', ','), str(t_time).replace('.', ',')) if v_real > v_max else '\\True Nếu camera ghi nhận được hình ảnh biển số xe ô tô liên tục trong một khoảng thời gian kéo dài đúng $%s$ giây, và khoảng thời gian $%s$ giây này kết thúc đồng thời với thời điểm xe vừa ra khỏi vùng nhận diện tốt nhất, thì ôtô không vượt quá tốc độ cho phép' % (str(t_time).replace('.', ','), str(t_time).replace('.', ','))
            vdc_da_1_s = 'Nếu camera ghi nhận được hình ảnh biển số xe ô tô liên tục trong một khoảng thời gian kéo dài đúng $%s$ giây, và khoảng thời gian $%s$ giây này kết thúc đồng thời với thời điểm xe vừa ra khỏi vùng nhận diện tốt nhất, thì ôtô đã vượt quá tốc độ cho phép' % (str(t_time).replace('.', ','), str(t_time).replace('.', ',')) if v_real <= v_max else 'Nếu camera ghi nhận được hình ảnh biển số xe ô tô liên tục trong một khoảng thời gian kéo dài đúng $%s$ giây, và khoảng thời gian $%s$ giây này kết thúc đồng thời với thời điểm xe vừa ra khỏi vùng nhận diện tốt nhất, thì ôtô không vượt quá tốc độ cho phép' % (str(t_time).replace('.', ','), str(t_time).replace('.', ','))
            list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
            vdc_da_1=random.choice(list_vdc_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải
            ketluan_vdc = "vượt quá" if v_real > v_max else "không vượt quá"
            loigiai_vdc_1 = ('''Áp dụng định lý Talet: $\\frac{EF}{DI} = \\frac{AF}{AI} = \\frac{%s - %s}{%s - %s} \\Rightarrow EF = %s$. \\\\
            Suy ra $v = \\frac{s}{t} = \\frac{EF}{t} = \\frac{%s}{%s} \\approx %s$ (km/h). \\\\
            Vậy xe %s tốc độ cho phép.'''
            % (str(abs(y_A)).replace('.', ','), str(abs(y_M)).replace('.', ','),
               str(abs(y_A)).replace('.', ','), str(abs(y_D)).replace('.', ','),
               EF_str,
               EF_str, str(t_time).replace('.', ','), v_real_str,
               ketluan_vdc))

            # Đưa các lời giải vào danh sách lời giải
            list_vdc_2 = [loigiai_vdc_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_vdc = list(zip(list_vdc_1, list_vdc_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_vdc)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Lặp đến khi đáp án có từ 1 đến 3 đúng
            while True:
                nb_da_1 = random.choice(list_nb_da_1)
                th_da_1 = random.choice(list_th_da_1)
                vd_da_1 = random.choice(list_vd_da_1)
                vdc_da_1 = random.choice(list_vdc_da_1)

                answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
                true_count = count_true_answers(answers)

                if 1 <= true_count <= 3:
                    break

            # Gán lại vào list
            list_nb_1 = [nb_da_1]
            list_th_1 = [th_da_1]
            list_vd_1 = [vd_da_1]
            list_vdc_1 = [vdc_da_1]

            combined_nb = list(zip(list_nb_1, list_nb_2))
            combined_th = list(zip(list_th_1, list_th_2))
            combined_vd = list(zip(list_vd_1, list_vd_2))
            combined_vdc = list(zip(list_vdc_1, list_vdc_2))

            random.shuffle(combined_nb)
            random.shuffle(combined_th)
            random.shuffle(combined_vd)
            random.shuffle(combined_vdc)

            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+
                str(noidungcauhoi)+ '\n' +
                '\\choiceTFn \n'
                '{'+str(shuffled_answers_nb[0])+'}\n'
                '{'+str(shuffled_answers_th[0])+'}\n'
                '{'+str(shuffled_answers_vd[0])+'}\n'
                '{'+str(shuffled_answers_vdc[0])+'}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item '+str(shuffled_solutions_nb[0])+'\n'
                '\\item '+str(shuffled_solutions_th[0])+'\n'
                '\\item '+str(shuffled_solutions_vd[0])+'\n'
                '\\item '+str(shuffled_solutions_vdc[0])+'\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n'
                '\\end{minipage}\n\n')
            return content 

