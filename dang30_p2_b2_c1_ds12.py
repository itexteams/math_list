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


def bt_dang30_p2_b2_c1_ds12(self):
            # Khai báo biến
            # Khai báo biến
            x = symbols('x')

            # --- THUẬT TOÁN NGẪU NHIÊN HÓA (RANDOM) ---
            # Chọn bán kính đáy hình nón r từ {2, 3}
            r = random.choice([2, 3])       
            # Chọn tỉ lệ k = l / r từ {2, 3} để số liệu cực trị và phép chia luôn đẹp
            k = random.choice([2, 3])       
            # Chiều cao hình nón l
            l = k * r                       

            # --- CÁC ĐẠI LƯỢNG TOÁN HỌC ---
            # Chiều cao khối trụ h = l - k*x
            h_expr = l - k*x
            # Thể tích khối trụ V = pi * x^2 * (l - k*x)
            V_expr = pi * (l*x**2 - k*x**3)

            # TH1: Bán kính đáy bằng chiều cao (x = h) => x = l - k*x => x = l / (k + 1)
            x_equal = Rational(l, k + 1)
            V_equal = pi * x_equal**3

            # TH2: Thể tích lớn nhất đạt tại x_max = 2*r/3
            x_max = Rational(2*r, 3)
            V_max = Rational(4*r**2 * l, 27) * pi

            # Nội dung câu hỏi (Đã sửa cú pháp TikZ 'to' thành 'and' và loại bỏ ký tự % chú thích để tránh lỗi format)
            noidungcauhoi = ('''Một khúc gỗ có dạng hình khối nón có bán kính đáy $r = %s\\text{m}$, chiều cao $l = %s\\text{m}$. Bác thợ mộc chế tác từ khúc gỗ đó thành một khúc gỗ có dạng hình khối trụ như hình vẽ.\\\\
            \\begin{center}
            \\begin{tikzpicture}[x=0.75pt,y=0.75pt,yscale=-1,xscale=1]
            	\\draw [line width=1]    (169,51.6) -- (238,200.6) ;
            	\\draw [line width=1]    (169,51.6) -- (100,200.6) ;
            	\\draw  [dash pattern={on 5.63pt off 4.5pt}][line width=1]  (131.5,200.6) .. controls (131.5,194.6) and (148.29,189.73) .. (169,189.73) .. controls (189.71,189.73) and (206.5,194.6) .. (206.5,200.6) .. controls (206.5,206.6) and (189.71,211.47) .. (169,211.47) .. controls (148.29,211.47) and (131.5,206.6) .. (131.5,200.6) -- cycle ;
            	\\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (100,200.6) -- (238,200.6) ;
            	\\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (169,51.6) -- (169,200.6) ;
            	\\draw  [dash pattern={on 5.63pt off 4.5pt}][line width=1]  (131.5,134.6) .. controls (131.5,128.6) and (148.29,123.73) .. (169,123.73) .. controls (189.71,123.73) and (206.5,128.6) .. (206.5,134.6) .. controls (206.5,140.6) and (189.71,145.47) .. (169,145.47) .. controls (148.29,145.47) and (131.5,140.6) .. (131.5,134.6) -- cycle ;
            	\\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (131.5,134.6) -- (131.5,200.6) ;
            	\\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (206.5,134.6) -- (206.5,200.6) ;
            	\\draw  [draw opacity=0][line width=1]  (238,202.15) .. controls (238,202.22) and (238,202.28) .. (238,202.35) .. controls (238,214.25) and (207.22,223.9) .. (169.25,223.9) .. controls (131.28,223.9) and (100.5,214.25) .. (100.5,202.35) .. controls (100.5,202.05) and (100.52,201.75) .. (100.56,201.45) -- (169.25,202.35) -- cycle ; \\draw  [line width=1]  (238,202.15) .. controls (238,202.22) and (238,202.28) .. (238,202.35) .. controls (238,214.25) and (207.22,223.9) .. (169.25,223.9) .. controls (131.28,223.9) and (100.5,214.25) .. (100.5,202.35) .. controls (100.5,202.05) and (100.52,201.75) .. (100.56,201.45) ;  
            	\\draw  [draw opacity=0][dash pattern={on 5.63pt off 4.5pt}][line width=1]  (100.56,199.9) .. controls (100.56,199.84) and (100.56,199.77) .. (100.56,199.7) .. controls (100.56,187.8) and (131.34,178.15) .. (169.31,178.15) .. controls (207.28,178.15) and (238.06,187.8) .. (238.06,199.7) .. controls (238.06,200) and (238.04,200.3) .. (238,200.6) -- (169.31,199.7) -- cycle ; \\draw  [dash pattern={on 5.63pt off 4.5pt}][line width=1]  (100.56,199.9) .. controls (100.56,199.84) and (100.56,199.77) .. (100.56,199.7) .. controls (100.56,187.8) and (131.34,178.15) .. (169.31,178.15) .. controls (207.28,178.15) and (238.06,187.8) .. (238.06,199.7) .. controls (238.06,200) and (238.04,200.3) .. (238,200.6) ;  
            	\\draw  [draw opacity=0][line width=1]  (206.49,134.4) .. controls (206.5,134.47) and (206.5,134.53) .. (206.5,134.6) .. controls (206.5,140.6) and (189.6,145.47) .. (168.75,145.47) .. controls (147.9,145.47) and (131,140.6) .. (131,134.6) .. controls (131,134.2) and (131.08,133.8) .. (131.22,133.41) -- (168.75,134.6) -- cycle ; \\draw  [line width=1]  (206.49,134.4) .. controls (206.5,134.47) and (206.5,134.53) .. (206.5,134.6) .. controls (206.5,140.6) and (189.6,145.47) .. (168.75,145.47) .. controls (147.9,145.47) and (131,140.6) .. (131,134.6) .. controls (131,134.2) and (131.08,133.8) .. (131.22,133.41) ;  
            	\\draw [line width=1]  [dash pattern={on 5.63pt off 4.5pt}]  (131.22,133.41) -- (206.49,134.4) ;
            	\\draw  [dash pattern={on 5.63pt off 4.5pt}][line width=1]  (285.5,200.6) .. controls (285.5,194.6) and (302.29,189.73) .. (323,189.73) .. controls (343.71,189.73) and (360.5,194.6) .. (360.5,200.6) .. controls (360.5,206.6) and (343.71,211.47) .. (323,211.47) .. controls (302.29,211.47) and (285.5,206.6) .. (285.5,200.6) -- cycle ;
            	\\draw  [line width=1]  (285.5,134.6) .. controls (285.5,128.6) and (302.29,123.73) .. (323,123.73) .. controls (343.71,123.73) and (360.5,128.6) .. (360.5,134.6) .. controls (360.5,140.6) and (343.71,145.47) .. (323,145.47) .. controls (302.29,145.47) and (285.5,140.6) .. (285.5,134.6) -- cycle ;
            	\\draw [line width=1]    (285.5,134.6) -- (285.5,200.6) ;
            	\\draw [line width=1]    (360.5,134.6) -- (360.5,200.6) ;
            	\\draw  [draw opacity=0][line width=1]  (360.74,200.4) .. controls (360.75,200.47) and (360.75,200.53) .. (360.75,200.6) .. controls (360.75,206.6) and (343.85,211.47) .. (323,211.47) .. controls (302.15,211.47) and (285.25,206.6) .. (285.25,200.6) .. controls (285.25,200.2) and (285.33,199.8) .. (285.47,199.41) -- (323,200.6) -- cycle ; \\draw  [line width=1]  (360.74,200.4) .. controls (360.75,200.47) and (360.75,200.53) .. (360.75,200.6) .. controls (360.75,206.6) and (343.85,211.47) .. (323,211.47) .. controls (302.15,211.47) and (285.25,206.6) .. (285.25,200.6) .. controls (285.25,200.2) and (285.33,199.8) .. (285.47,199.41) ;  
            \\end{tikzpicture}
            \\end{center}
            Xét tính đúng sai của các mệnh đề sau:''' 
                             %(latex(r), latex(l)))

            ########################################################################
            # Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True Đặt $x$ là bán kính đáy hình trụ ($0 < x < %s$), chiều cao của khối trụ tính theo bán kính đáy hình trụ là $h = -%sx + %s$' %(latex(r), latex(k), latex(l))
            nb_da_1_s = 'Đặt $x$ là bán kính đáy hình trụ ($0 < x < %s$), chiều cao của khối trụ tính theo bán kính đáy hình trụ là $h = %sx - %s$' %(latex(r), latex(k), latex(l))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = ('''Ta có mặt cắt qua trục hình nón như hình vẽ.\\\\
            \\begin{center}
            \\begin{tikzpicture}[scale=0.8, line width=1pt]
            \\coordinate (S) at (0,4);
            \\coordinate (A) at (-2.5,0);
            \\coordinate (B) at (2.5,0);
            \\coordinate (I) at (0,0);
            \\coordinate (Ap) at (-1.25,2);
            \\coordinate (Bp) at (1.25,2);
            \\coordinate (Ip) at (0,2);
            \\draw (A) -- (S) -- (B) -- cycle;
            \\draw (Ap) -- (Bp);
            \\draw (I) -- (S);
            \\draw (-1.25,0) -- (Ap);
            \\draw (1.25,0) -- (Bp);
            \\draw[fill=black] (S) circle (1.5pt) node[above] {$S$};
            \\draw[fill=black] (A) circle (1.5pt) node[left] {$A$};
            \\draw[fill=black] (B) circle (1.5pt) node[right] {$B$};
            \\draw[fill=black] (I) circle (1.5pt) node[below] {$I$};
            \\draw[fill=black] (Ap) circle (1.5pt) node[left] {$A\'$};
            \\draw[fill=black] (Bp) circle (1.5pt) node[right] {$B\'$};
            \\draw[fill=black] (Ip) circle (1.5pt) node[above right] {$I\'$};
            \\node at (-0.6, 1) {$h$};
            \\node at (0.6, 0.2) {$r$};
            \\end{tikzpicture}
            \\end{center}
            Ta có hai tam giác $SAI$ và $SA\'I\'$ đồng dạng $\\Rightarrow \\frac{SI}{SI\'} = \\frac{AI}{A\'I\'} \\Leftrightarrow \\frac{%s}{%s - h} = \\frac{%s}{x} \\Rightarrow h = %s - %sx$, với $0 < x < %s$.'''
                            %(latex(l), latex(l), latex(r), latex(l), latex(k), latex(r)))

            # Đưa các lời giải vào danh sách lời giải
            list_nb_2 = [loigiai_nb_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_nb = list(zip(list_nb_1, list_nb_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_nb)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ########################################################################
            # Thông hiểu ############################################
            # Các đáp án
            th_da_1_d = 'Hàm số xác định thể tích của khối trụ trên là $V = \\pi \\left( %sx^2 - %sx^3 \\right) \\text{m}^3$, $\\forall x \\in (0; %s)$' %(latex(l), latex(k), latex(r))
            th_da_1_s = '\\True Hàm số xác định thể tích của khối trụ trên là $V = \\pi \\left( %sx^2 - %sx^3 \\right) \\text{m}^3$, $\\forall x \\in (0; %s)$' %(latex(l), latex(k), latex(r))
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1]

            # Nội dung lời giải
            loigiai_th_1 = ('''Thể tích của khối trụ là: $V = \\pi \\cdot x^2 \\cdot h = \\pi \\cdot x^2 \\cdot (%s - %sx) = \\pi \\left( %sx^2 - %sx^3 \\right)$, với $0 < x < %s$.'''
                            %(latex(l), latex(k), latex(l), latex(k), latex(r)))

            # Đưa các lời giải vào danh sách lời giải
            list_th_2 = [loigiai_th_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_th = list(zip(list_th_1, list_th_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_th)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ######################################################################## 
            # Vận dụng ############################################
            # Các đáp án
            vd_da_1_d = '\\True Giả sử bác thợ mộc chế tác khúc gỗ đó thành hình trụ có bán kính đáy bằng chiều cao, khi đó thể tích của khối trụ là $V = %s \\text{m}^3$' %(latex(V_equal))
            vd_da_1_s = 'Giả sử bác thợ mộc chế tác khúc gỗ đó thành hình trụ có bán kính đáy bằng chiều cao, khi đó thể tích của khối trụ là $V = %s \\text{m}^3$' %(latex(V_equal * 2))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            loigiai_vd_1 = ('''Bác thợ mộc chế tác khúc gỗ đó thành hình trụ có bán kính đáy bằng chiều cao:\\\\
            Suy ra: $x = %s - %sx \\Rightarrow x = %s$.\\\\
            Khi đó thể tích của khối trụ là:\\\\
            $V = \\pi \\cdot x^3 = \\pi \\cdot \\left( %s \\right)^3 = %s \\text{m}^3$.'''
                            %(latex(l), latex(k), latex(x_equal), latex(x_equal), latex(V_equal)))

            # Đưa các lời giải vào danh sách lời giải
            list_vd_2 = [loigiai_vd_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_vd = list(zip(list_vd_1, list_vd_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_vd)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ######################################################################## 
            # Vận dụng cao ############################################
            # Các đáp án
            vdc_da_1_d = '\\True Thể tích lớn nhất của khối gỗ mà bác thợ mộc chế tác là $V_{\\max} = %s \\text{m}^3$' %(latex(V_max))
            vdc_da_1_s = 'Thể tích lớn nhất của khối gỗ mà bác thợ mộc chế tác là $V_{\\max} = %s \\text{m}^3$' %(latex(V_max * 2))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải
            loigiai_vdc_1 = ('''Xét hàm số $V(x) = \\pi \\left( -%sx^3 + %sx^2 \\right)$ với $0 < x < %s$.\\\\
            Đạo hàm $V\'(x) = \\pi \\left( -%sx^2 + %sx \\right)$.\\\\
            Giải phương trình $V\'(x) = 0 \\Leftrightarrow \\pi \\left( -%sx^2 + %sx \\right) = 0 \\Leftrightarrow \\left[ \\begin{aligned} &x = 0 \\quad (l) \\\\ &x = %s \\quad (n) \\end{aligned} \\right. $\\\\
            Bảng biến thiên:\\\\
            \\begin{center}
            \\begin{tikzpicture}
            \\tkzTabInit[espcl=2.5,lgt=1.5]
            {$x$/1,$V\'$/0.7,$V$/2.1}
            {$0$,$%s$,$%s$}
            \\tkzTabLine{,+,0,-,}
            \\tkzTabVar{-/$0$,+/$%s$,-/$0$}
            \\end{tikzpicture}
            \\end{center}
            Dựa vào bảng biến thiên ta thấy $V_{\\max} = %s \\text{m}^3$ khi $x = %s$.'''
                             %(latex(k), latex(l), latex(r), latex(3*k), latex(2*l), latex(3*k), latex(2*l), latex(x_max), latex(x_max), latex(r), latex(V_max), latex(V_max), latex(x_max)))

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
            str(noidungcauhoi)+ 
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
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

