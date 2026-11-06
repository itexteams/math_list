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


def bt_dang8_p2_b3_c1_hh12(self):
            # Khai báo biến
            # Khai báo biến
            h_D = randint(200, 250)
            h_A = randint(50, 100)
            d_A = randint(300, 400)
            d_M = randint(150, d_A - 20)

            # Các giá trị tính toán trước
            h_diff = h_D - h_A
            dM_minus_dA = d_M - d_A

            AD_len = math.sqrt(d_A**2 + h_diff**2)
            AD_len_str = f"{AD_len:.2f}".replace('.', ',')
            AD_len_false = f"{(AD_len + randint(5, 15)):.2f}".replace('.', ',')

            MN_len = h_diff * (d_A - d_M) / d_A
            MN_len_str = f"{MN_len:.2f}".replace('.', ',')
            MN_len_false = f"{(MN_len + 5):.2f}".replace('.', ',')

            zN_val = MN_len + h_A
            zN_str = f"{zN_val:.2f}".replace('.', ',')

            hinhve=r'''\scalebox{0.9}{ 	\begin{tikzpicture}[scale=1,font=\footnotesize,line join=round, line cap=round, >=stealth]
            		\definecolor{deepskyblue}{rgb}{0.0, 0.75, 1.0}
            		\fill[top color=deepskyblue!60,middle color=white] (-0.5,0.3)--(6,1)--(6,4)--(-0.5,4)--cycle;
            		\fill[opacity=0.8, bottom color= cyan!50!white, top color= cyan!20!white] (-0.5,-1.7)--(6,-1.7)-- (6,1)--(-0.5,0.3)--cycle;
            		\def \Va{(-0.09,0.56) .. controls +(70:0.3) and +(-100:0.2)..(0.07,1.65) .. controls +(-65:1.55) and +(-114:2.92) .. (2.67,3.25) .. controls +(-60:0.6) and +(140:0.93) .. (4.4,1.27)}
            		\def \Vb{(0.28,1.62) .. controls +(-61.9:1.53) and +(-115.0:2.78) .. (3.08,3.25) .. controls +(-60.6:0.42) and +(149.8:0.93) .. (4.92,1.30)}
            		\fill[pattern={Lines[angle=90,distance=2.75pt]},
            		pattern color=brown!80] \Vb-- (6,1.35) .. controls +(-177.5:2.94) and +(15.7:1.52) .. (0.27,0.64) --cycle;
            		\draw [brown!80!black, line width=1] \Vb;
            		\tikzset{tru/.pic={ 
            				\fill[black!20!red] (2.73,3.31)	.. controls +(-20:0.1) and +(-160:0.1) .. (3.06,3.31)-- (3.06,3.14) .. controls +(160:0.1) and +(20:0.1) .. (2.73,3.14) -- cycle
            				(2.73,2.82) .. controls +(-20:0.1) and +(-160:0.1) .. (3.06,2.83) -- (3.06,2.68) .. controls +(160:0.1) and +(20:0.1) .. (2.73,2.68) -- cycle
            				(2.73,2.36)  .. controls +(-20:0.1) and +(-160:0.1) .. (3.06,2.36) -- (3.06,2.19) .. controls +(160:0.1) and +(20:0.1) .. (2.73,2.19) -- cycle
            				(2.73,1.77) .. controls +(-20:0.1) and +(-160:0.1) .. (3.06,1.76) -- (3.06,1.55) .. controls +(160:0.1) and +(20:0.1) .. (2.73,1.56) -- cycle;
            				\fill[brown!40!red] (3.06,0.25) -- (3.17,0.25) -- (3.14,3.31) -- (3.06,3.31) -- cycle;	}}
            		\draw [line width=2, red!40!black] (2.81,0.93) -- (3.06,0.68) -- (2.75,0.30) -- (3.06,0.31) -- (2.75,0.67) -- (2.98,0.96)	
            		(3.04,0.69) -- (2.75,0.68);
            		\draw [line width=1, red!40!black] (0.13,0.49) -- (0.25,0.36) -- (0.1,0.17) -- (0.25,0.17) -- (0.1,0.36) -- (0.21,0.5)	(0.24,0.36) -- (0.1,0.36);
            		\path 
            		(0,0) pic[scale=1]{tru}
            		(-1.28,0.02) pic[scale=0.5]{tru}
            		(2.65,0.19) coordinate (O)
            		(4.33,1.32) coordinate (A)
            		(2.65,3.29) coordinate (D)
            		(3.5,1.1) coordinate (M)
            		(3.5,1.7) coordinate (N);
            		\fill[brown!80]  (4.45,0.56) .. controls +(90:0.35) and +(90:0.35) .. (4.95,0.58)-- (5.06,0.58) -- (5.06,1.11)--(4.35,1.06)-- (4.35,0.56) -- cycle;
            		\fill[pattern=grid, pattern color=black!20!brown]  (4.45,0.56) .. controls +(90:0.35) and +(90:0.35) .. (4.95,0.58)-- (5.06,0.58) -- (5.06,1.11)--(4.35,1.06)-- (4.35,0.56) -- cycle;
            		\fill[left color=gray,right color=white] (5.06,0.58) rectangle (5.11,1.37);
            		\fill[black!20!red] (-0.09,0.46) .. controls +(13.5:1.44) and +(-177.2:2.88) .. (6,1.16)--(6,1.35) .. controls +(-177.8:2.93) and +(16.1:1.52) .. (-0.09,0.55)--cycle;
            		\draw (-0.09,0.46) .. controls +(13.5:1.44) and +(-177.2:2.88) .. (6,1.16);
            		\begin{scope}
            			\clip \Va-- (6,1.35) .. controls +(-177.7:2.94) and +(15.6:1.68) .. (0.072,0.59) --cycle;
            			\foreach \x in {0,1,...,50}
            			\draw[brown!80] ({0.1*\x},0)--({0.1*\x},4);
            		\end{scope}
            		\draw [brown!80!black, line width=1] \Va;
            		\fill[brown!40!red] (O) -- (2.75,0.19) -- (2.73,3.31) -- (2.65,3.31) -- cycle
            		(0.04,0.11) -- (0.1,0.11) -- (0.09,1.68) -- (0.06,1.68) -- cycle;
            		\fill[left color=gray,right color=white] (4.3,0.55) rectangle (4.35,1.32);
            		\draw[->,thick] (O)--+(-150:1.5) node[below]{$x$};
            		\draw[->,thick] (O)--+(1:1.5) node[below]{$y$};
            		\draw[->,thick] (O)--+(90:3.5) node[right]{$z$};
            		\draw[thick,blue] (M)--(N);
            		\foreach \i/\g in {A/170,D/180,O/-60,M/-90,N/90}
            		\fill (\i) circle(1pt)+(\g:2.5mm)node{$\i$};
            	\end{tikzpicture} }'''

            # Nội dung câu hỏi
            noidungcauhoi = (r'''\immini{Hình dưới đây là hình ảnh Cầu Cổng Vàng (The Golden Gate Bridge) ở Mỹ. Xét hệ trục tọa độ $Oxyz$ (như hình vẽ) với $O$ là điểm nằm trên bệ của chân cột trụ tại mặt nước, trục $Oz$ trùng với cột trụ, mặt phẳng $(Oxy)$ là mặt nước và trục $Oy$ cùng phương với cầu (đơn vị trên hệ trục tọa độ là mét). Dây cáp $AD$ (xem như một đoạn thẳng) nối điểm $D$ thuộc trục $Oz$ với một điểm $A$ thuộc mặt phẳng $(Oyz)$.
            Biết điểm $D$ là đỉnh cột trụ, cách mặt nước $%s$ m; điểm $A$ cách mặt nước $%s$ m và cách trục $Oz$ một khoảng bằng $%s$ m.}{%s}''' 
                             % (h_D, h_A, d_A, hinhve))

            ######################################################################## Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True Tọa độ điểm $D$ là $(0;0;%s)$' % (h_D)
            nb_da_1_s = 'Tọa độ điểm $D$ là $(%s;0;0)$' % (h_D)
            list_nb_da_1=[nb_da_1_d,nb_da_1_s]
            nb_da_1=random.choice(list_nb_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = ('''Vì điểm $D$ là đỉnh cột trụ, cách mặt nước (mặt phẳng $(Oxy)$) một khoảng là $%s$ m và nằm trên trục $Oz$ nên $D(0;0;%s)$.'''
                            % (h_D, h_D))

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
            th_da_1_d = '\\True Tọa độ của vectơ $\\overrightarrow{AD}$ là $(0;-%s;%s)$' % (d_A, h_diff)  
            th_da_1_s = 'Tọa độ của vectơ $\\overrightarrow{AD}$ là $(0;%s;-%s)$' % (d_A, h_diff)
            list_th_da_1=[th_da_1_d,th_da_1_s]
            th_da_1=random.choice(list_th_da_1)


            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1]

            # Nội dung lời giải
            loigiai_th_1 = ('''Điểm $A$ thuộc mặt phẳng $(Oyz)$ nên $x_A = 0$. $A$ cách mặt nước $%s$ m nên $z_A = %s$. Điểm $A$ cách trục $Oz$ một khoảng $%s$ m, dựa vào hình vẽ $A$ nằm ở phần dương của trục $Oy$ nên $y_A = %s$. Vậy $A(0;%s;%s)$.\\\\
            Ta có $\\overrightarrow{AD} = (0 - 0; 0 - %s; %s - %s) = (0; -%s; %s)$.'''       
                       % (h_A, h_A, d_A, d_A, d_A, h_A, d_A, h_D, h_A, d_A, h_diff))

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
            vd_da_1_d = '\\True Độ dài dây cáp $AD$ là $%s$ m (kết quả làm tròn đến hàng phần trăm)' % (AD_len_str)
            vd_da_1_s = 'Độ dài dây cáp $AD$ là $%s$ m (kết quả làm tròn đến hàng phần trăm)' % (AD_len_false)
            list_vd_da_1=[vd_da_1_d,vd_da_1_s]
            vd_da_1=random.choice(list_vd_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            loigiai_vd_1 = ('''Độ dài dây cáp $AD$ là $|\\overrightarrow{AD}| = \\sqrt{0^2 + (-%s)^2 + %s^2} \\approx %s$ (m).'''  
                       % (d_A, h_diff, AD_len_str))

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
            vdc_da_1_d = ('\\True Người ta dùng một đoạn đèn led trang trí nối thẳng từ điểm $N$ trên dây cáp $AD$ '
                          'đến điểm $M$ trên thành cầu, biết $M$ cách mặt nước $%s$ m, cách trục $Oz$ một khoảng bằng $%s$ m '
                          'và $MN$ song song với cột trụ. Độ dài đoạn đèn led cần dùng là $%s$ m '
                          '(kết quả làm tròn đến hàng phần trăm)') % (h_A, d_M, MN_len_str) 

            vdc_da_1_s = ('Người ta dùng một đoạn đèn led trang trí nối thẳng từ điểm $N$ trên dây cáp $AD$ '
                          'đến điểm $M$ trên thành cầu, biết $M$ cách mặt nước $%s$ m, cách trục $Oz$ một khoảng bằng $%s$ m '
                          'và $MN$ song song với cột trụ. Độ dài đoạn đèn led cần dùng là $%s$ m '
                          '(kết quả làm tròn đến hàng phần trăm)') % (h_A, d_M, MN_len_false)

            list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
            vdc_da_1=random.choice(list_vdc_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải
            loigiai_vdc_1 = ('''Thành cầu song song với mặt nước và nằm ngang nên điểm $A$ và điểm $M$ đều có cùng cao độ, do đó $z_M = z_A = %s$. Điểm $M$ thuộc mặt phẳng $(Oyz)$ nên $x_M=0$. Do $M$ cách trục $Oz$ một đoạn $%s$ m nên $y_M = %s$, suy ra $M(0;%s;%s)$.\\\\
            Vì đoạn đèn led $MN$ song song với cột trụ (trục $Oz$) nên $N$ có cùng hoành độ và tung độ với $M$. Do đó $N$ có tọa độ $x_N = 0, y_N = %s$. Giả sử $N(0;%s;z_N)$.\\\\
            Ta có $\\overrightarrow{AN} = (0; %s; z_N - %s)$.\\\\
            Vì $A, N, D$ thẳng hàng nên $\\overrightarrow{AN}$ cùng phương với $\\overrightarrow{AD} = (0; -%s; %s)$.\\\\
            Suy ra $\\frac{%s}{-%s} = \\frac{z_N - %s}{%s} \\Rightarrow z_N - %s = \\frac{%s \\cdot %s}{-%s} \\Rightarrow z_N \\approx %s$.\\\\
            Độ dài đoạn đèn led là $MN = z_N - z_M \\approx %s - %s = %s$ (m).'''
                       % (h_A, d_M, d_M, d_M, h_A,
                          d_M, d_M, dM_minus_dA, h_A,
                          d_A, h_diff,
                          dM_minus_dA, d_A, h_A, h_diff, h_A, dM_minus_dA, h_diff, d_A, zN_str,
                          zN_str, h_A, MN_len_str))

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
                str(noidungcauhoi)+ '\n'
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
                '\\end{ex}\n\\end{minipage}\n\n')
            return content

