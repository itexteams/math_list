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


def bt_dang9_p2_b3_c1_hh12(self):
            # Khai báo biến
            # Khai báo biến
            t = symbols('t')

            # Khởi tạo thông số ngẫu nhiên cho bài toán
            m = random.choice([1, 2])
            k = random.choice([3, 4, 5, 6, 7])
            L = random.randint(10, 30)

            xA, yA, zA = -2*m, 8*m, 0
            xB, yB, zB = 0, 0, -2*m
            xC, yC, zC = 0, 4*m, 0

            SC_val = 3 * k

            # Nội dung câu hỏi
            noidungcauhoi = ('''Trong không gian với hệ trục tọa độ $Oxyz$ , cho hình chóp $S.ABC$ với tọa độ các đỉnh lần lượt là $A(%s;%s;%s); B(%s;%s;%s); C(%s;%s;%s)$. Biết rằng $SC \\perp (ABC)$; $SC = %s$ , trong đó hai đỉnh $S$ và $O$ nằm ở hai phía khác nhau so với mặt phẳng $(ABC)$.'''               
                             %(xA, yA, zA, xB, yB, zB, xC, yC, zC, SC_val))

            ########################################################################
            # Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True $\\overrightarrow{n}_{(ABC)} = (2; 1; -2)$'
            nb_da_1_s = '$\\overrightarrow{n}_{(ABC)} = (1; 2; -2)$'
            list_nb_da_1=[nb_da_1_d,nb_da_1_s]
            nb_da_1=random.choice(list_nb_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = ('''Ta có: $\\overrightarrow{AB} = (%s; %s; %s)$ và $\\overrightarrow{AC} = (%s; %s; 0)$.\\\\
            Vectơ pháp tuyến của mặt phẳng $(ABC)$ là: $\\overrightarrow{n}_{(ABC)} = [\\overrightarrow{AB}, \\overrightarrow{AC}] = (%s; %s; %s) = %s(2; 1; -2)$.\\\\
            Phương trình mặt phẳng $(ABC)$ đi qua $C(0;%s;0)$ là: $(ABC): 2x + y - 2z - %s = 0$.'''
            % (2*m, -8*m, -2*m, 2*m, -4*m, -8*m**2, -4*m**2, 8*m**2, -4*m**2, 4*m, 4*m))

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
            S_sum = k + 4*m
            th_da_1_d = '\\True Điểm $S$ nằm trên mặt phẳng $x + y + z = %s$' % (S_sum)
            th_da_1_s = 'Điểm $S$ nằm trên mặt phẳng $x + y + z = %s$' % (S_sum + random.choice([-2, -1, 1, 2]))
            list_th_da_1=[th_da_1_d,th_da_1_s]
            th_da_1=random.choice(list_th_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1]

            # Nội dung lời giải
            loigiai_th_1 = ('''Vì $SC \\perp (ABC)$ nên đường thẳng $SC$ nhận $\\overrightarrow{n}_{(ABC)} = (2; 1; -2)$ làm vectơ chỉ phương.\\\\
            Tọa độ điểm $S$ có dạng: $S(2k_1; %s+k_1; -2k_1)$ (với $k_1$ là tham số).\\\\
            Độ dài $SC = %s \\Leftrightarrow \\sqrt{(2k_1)^2 + k_1^2 + (-2k_1)^2} = %s \\Leftrightarrow 3|k_1| = %s \\Leftrightarrow k_1 = \\pm %s$.\\\\
            Xét vị trí của $S$ và gốc tọa độ $O(0;0;0)$ đối với mặt phẳng $(ABC)$:\\\\
            Thay $O(0;0;0)$ vào $(ABC)$ thì ta có $f(0;0;0) = %s < 0$.\\\\
            Vậy để $S$ và $O$ nằm khác phía, ta cần tính $f(S) > 0$.\\\\
            Với $k_1 = %s \\Rightarrow S(%s; %s; %s)$ ta có $f(S) = %s > 0$ (thỏa mãn).\\\\
            Với $k_1 = %s \\Rightarrow S(%s; %s; %s)$ ta có $f(S) = %s < 0$ (loại).\\\\
            Vậy $S(%s; %s; %s)$ thay vào $x+y+z$ ta thấy $%s + %s + (%s) = %s$.'''
            % (4*m, 3*k, 3*k, 3*k, k, -4*m, k, 2*k, 4*m+k, -2*k, 9*k, -k, -2*k, 4*m-k, 2*k, -9*k, 2*k, 4*m+k, -2*k, 2*k, 4*m+k, -2*k, S_sum))

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
            V = 6 * (m**2) * k
            vd_da_1_d = '\\True Thể tích khối chóp $S.ABC$ bằng $%s$' % (V)
            vd_da_1_s = 'Thể tích khối chóp $S.ABC$ bằng $%s$' % (3 * V)
            list_vd_da_1=[vd_da_1_d,vd_da_1_s]
            vd_da_1=random.choice(list_vd_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            loigiai_vd_1 = ('''Diện tích tam giác đáy $ABC : S_{\\Delta ABC} = \\frac{1}{2} |[\\overrightarrow{AB}, \\overrightarrow{AC}]| = \\frac{1}{2} \\sqrt{(%s)^2 + (%s)^2 + (%s)^2} = \\frac{1}{2} \\cdot %s = %s$.\\\\
            Thể tích khối chóp: $V = \\frac{1}{3} S_{\\Delta ABC} \\cdot SC = \\frac{1}{3} \\cdot %s \\cdot %s = %s$.'''  
                       %(-8*m**2, -4*m**2, 8*m**2, 12*m**2, 6*m**2, 6*m**2, 3*k, V))

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
            while True:
                alpha = random.randint(2, 5)
                beta = random.randint(2, 4)
                gamma = random.randint(2, 5)
                val = alpha*(-m) + beta*(4*m) + gamma*(-m)
                if val != 0:
                    break

            sign = ">" if val > 0 else "<"
            wrong_sign = "<" if val > 0 else ">"

            # Các đáp án
            vdc_da_1_d = '\\True Xét điểm $T$ nằm trên tia đối của tia $SC$ thỏa mãn $ST = %s$. Khi đó, gọi $H(a;b;c)$ là hình chiếu vuông góc của $T$ lên đường thẳng $AB$ thì biểu thức $%sa + %sb + %sc %s 0$' % (L, alpha, beta, gamma, sign)
            vdc_da_1_s = 'Xét điểm $T$ nằm trên tia đối của tia $SC$ thỏa mãn $ST = %s$. Khi đó, gọi $H(a;b;c)$ là hình chiếu vuông góc của $T$ lên đường thẳng $AB$ thì biểu thức $%sa + %sb + %sc %s 0$' % (L, alpha, beta, gamma, wrong_sign)
            list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
            vdc_da_1=random.choice(list_vdc_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1]

            x_T_rat = sp.Rational(6*k + 2*L, 3)
            y_T_rat = sp.Rational(12*m + 3*k + L, 3)
            z_T_rat = sp.Rational(-6*k - 2*L, 3)

            CS_x, CS_y, CS_z = 2*k, k, -2*k

            ST_x = sp.Rational(L * CS_x, 3*k)
            ST_y = sp.Rational(L * CS_y, 3*k)
            ST_z = sp.Rational(L * CS_z, 3*k)

            TH_x = t - x_T_rat
            TH_y = -4*t - y_T_rat
            TH_z = -t - 2*m - z_T_rat

            # Nội dung lời giải
            loigiai_vdc_1 = ('''Tia $SC$ bắt đầu từ $S$ qua $C$. Tia đối của tia $SC$ cũng bắt đầu từ $S$ nhưng đi hướng ngược lại.\\\\
            Vì $T$ thuộc tia đối của $SC$ và $ST = %s$, vectơ $\\overrightarrow{ST}$ cùng hướng với $\\overrightarrow{CS} = (%s; %s; %s)$.\\\\
            $\\Rightarrow \\overrightarrow{ST} = \\frac{%s}{%s} \\overrightarrow{CS} = \\left(%s; %s; %s\\right) \\Rightarrow T\\left(%s; %s; %s\\right)$.\\\\
            Đường thẳng $AB$ đi qua $B(0;0;%s)$ có vectơ chỉ phương $\\overrightarrow{u} = \\frac{1}{%s} \\overrightarrow{AB} = (1; -4; -1)$.\\\\
            $H \\in AB \\Rightarrow H(t; -4t; %s - t)$ thì ta có $\\overrightarrow{TH} = \\left(%s; %s; %s\\right)$.\\\\
            Vì $TH \\perp AB$ nên $\\overrightarrow{TH} \\cdot \\overrightarrow{u} = 0 \\Leftrightarrow 1\\left(%s\\right) - 4\\left(%s\\right) - 1\\left(%s\\right) = 0 \\Leftrightarrow 18t + %s = 0 \\Leftrightarrow t = %s$.\\\\
            Tọa độ $H(%s; %s; %s)$.\\\\
            Biểu thức $%sa + %sb + %sc = %s(%s) + %s(%s) + %s(%s) = %s %s 0$.'''
                       %(L, CS_x, CS_y, CS_z,
                         L, 3*k, latex(ST_x), latex(ST_y), latex(ST_z), latex(x_T_rat), latex(y_T_rat), latex(z_T_rat),
                         -2*m, 2*m,
                         -2*m, latex(TH_x), latex(TH_y), latex(TH_z),
                         latex(TH_x), latex(TH_y), latex(TH_z), 18*m, -m,
                         -m, 4*m, -m,
                         alpha, beta, gamma, alpha, -m, beta, 4*m, gamma, -m, val, sign))

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
                '\\end{ex}\n \\end{minipage}\n\n')
            return content

