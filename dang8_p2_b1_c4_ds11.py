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


def bt_dang8_p2_b1_c4_ds11(self):
            # Khai báo biến
            # Giả sử cạnh tam giác ABC ban đầu là 'a_side'
            a_side = randint(1, 10) 

            # Các giá trị tính toán dựa trên lý thuyết hình học
            # Diện tích tam giác ABC ban đầu: S0 = (a^2 * sqrt(3)) / 4
            s0 = Rational(a_side**2, 4) * sqrt(3)
            # Chiều cao tam giác ABC ban đầu: h0 = (a * sqrt(3)) / 2
            h0 = Rational(a_side, 2) * sqrt(3)

            # Nội dung câu hỏi
            noidungcauhoi = (r'''\immini{Cho tam giác đều $ABC$ có độ dài cạnh bằng $%s$. Nối các trung điểm $A_1, B_1, C_1$ của các cạnh $BC, CA, AB$ ta được tam giác đều $A_1B_1C_1$. Tiếp tục quá trình này đến vô hạn. Gọi $S_n$ là diện tích của tam giác đều $A_nB_nC_n$ và $h_n$ là chiều cao của tam giác đó.}
                             {\scalebox{0.6}{
                                 \begin{tikzpicture}
            	\coordinate (A) at (0,6);
            	\coordinate (B) at (-3.46,0);
            	\coordinate (C) at (3.46,0);
            	\coordinate (C1) at (-1.73,3);
            	\coordinate (B1) at (1.73,3);
            	\coordinate (A1) at (0,0);
            	\coordinate (A2) at (0,3);
            	\coordinate (B2) at (-0.866,1.5);
            	\coordinate (C2) at (0.866,1.5);
            	\coordinate (C3) at (-0.433,2.25);
            	\coordinate (B3) at (0.433,2.25);
            	\coordinate (A3) at (0,1.5);
            	\draw[line width=1pt] (A)--(B)--(C)--cycle;
            	\draw[line width=1pt] (C1)--(B1)--(A1)--cycle;
            	\draw[line width=1pt] (A2)--(B2)--(C2)--cycle;
            	\draw[line width=1pt] (C3)--(B3)--(A3)--cycle;
            	\node[above] at (A) {$A$};
            	\node[below left] at (B) {$B$};
            	\node[below right] at (C) {$C$};
            	\node[left] at (C1) {$C_1$};
            	\node[right] at (B1) {$B_1$};
            	\node[below] at (A1) {$A_1$};
            	\node[above] at (A2) {$A_2$};
            	\node[left] at (B2) {$B_2$};
            	\node[right] at (C2) {$C_2$};
            	\node[left] at (C3) {$C_3$};
            	\node[right] at (B3) {$B_3$};
            	\node[below] at (A3) {$A_3$};
            \end{tikzpicture}}}''' 
                             % (latex(a_side)))

            ########################################################################
            # Nhận biết: Độ dài cạnh tam giác A1B1C1
            ########################################################################
            canh_a1 = Rational(a_side, 2)
            nb_da_1_d = r'\True Độ dài cạnh của tam giác $A_1B_1C_1$ bằng $%s$' % (latex(canh_a1))
            nb_da_1_s = r'Độ dài cạnh của tam giác $A_1B_1C_1$ bằng $%s$' % (latex(a_side))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            loigiai_nb_1 = (r'''Vì $B_1C_1$ là đường trung bình của tam giác $ABC$ nên $B_1C_1 = \frac{1}{2}BC = %s$.''' % (latex(canh_a1)))

            ########################################################################
            # Thông hiểu: Tính diện tích S3
            ########################################################################
            # S_n = S0 * (1/4)^n => S3 = S0 / 64
            s3_correct = s0 / 64
            th_da_1_d = r'\True Diện tích tam giác $A_3B_3C_3$ là $S_3 = %s$' % (latex(s3_correct))
            th_da_1_s = r'Diện tích tam giác $A_3B_3C_3$ là $S_3 = %s$' % (latex(s0 / 16))
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            loigiai_th_1 = (r'''Ta có $S_0 = %s$. Vì cạnh giảm một nửa thì diện tích giảm 4 lần, nên $S_n$ là CSN với $q=\frac{1}{4}$. Vậy $S_3 = S_0 \cdot \left(\frac{1}{4}\right)^3 = %s$.''' % (latex(s0), latex(s3_correct)))

            ########################################################################
            # Vận dụng: Tổng diện tích vô hạn (câu c trong hình)
            ########################################################################
            # lim u_n = S1 + S2 + ... = S1 / (1 - 1/4) = (S0/4) / (3/4) = S0/3
            s1 = s0 / 4
            sum_s_vohan = s1 / (1 - Rational(1, 4))
            vd_da_1_d = r'\True Tổng diện tích $u_n = S_1 + S_2 + \dots$ có giới hạn là $\frac{\sqrt{3}}{%s} \cdot %s$' % (3, latex(Rational(a_side**2, 4)))
            # Đơn giản hóa biểu thức cho đáp án
            vd_da_1_d = r'\True Giới hạn $\lim u_n = S_1 + S_2 + \dots = %s$' % (latex(sum_s_vohan))
            vd_da_1_s = r'Giới hạn $\lim u_n = S_1 + S_2 + \dots = %s$' % (latex(s0))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            loigiai_vd_1 = (r'''Dãy $\{S_n\}$ là cấp số nhân lùi vô hạn với $S_1 = %s$ và công bội $q=\frac{1}{4}$. Tổng là $L = \frac{S_1}{1-q} = %s$.''' % (latex(s1), latex(sum_s_vohan)))

            ########################################################################
            # Vận dụng cao: Tổng chiều cao vô hạn (câu d trong hình)
            ########################################################################
            # Trong hình, h1 được lấy là chiều cao tam giác ABC đầu tiên.
            # lim v_n = h1 + h2 + ... = h1 / (1 - 1/2) = 2*h1
            sum_h_vohan = h0 / (1 - Rational(1, 2))
            vdc_da_1_d = r'\True Tổng các chiều cao $v_n = h_1 + h_2 + \dots$ có giới hạn là $%s$' % (latex(sum_h_vohan))
            vdc_da_1_s = r'Tổng các chiều cao $v_n = h_1 + h_2 + \dots$ có giới hạn là $%s$' % (latex(h0))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            loigiai_vdc_1 = (r'''Chiều cao tam giác đầu tiên $h_1 = %s$. Các chiều cao sau bằng một nửa chiều cao trước, nên đây là CSN lùi vô hạn với $q=\frac{1}{2}$. Tổng là $\frac{h_1}{1-q} = 2h_1 = %s$.''' % (latex(h0), latex(sum_h_vohan)))

            # Logic trộn và đếm đáp án Đúng/Sai (giữ nguyên theo mẫu của bạn)
            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                ans_nb = random.choice(list_nb_da_1)
                ans_th = random.choice(list_th_da_1)
                ans_vd = random.choice(list_vd_da_1)
                ans_vdc = random.choice(list_vdc_da_1)

                current_answers = [ans_nb, ans_th, ans_vd, ans_vdc]
                if 1 <= count_true_answers(current_answers) <= 3:
                    break

            # Xuất kết quả theo định dạng LaTeX mẫu
            content = (r'\begin{minipage}{\textwidth}' + '\n'
                r'\begin{ex}' + '\n' + str(noidungcauhoi) + '\n'
                r'\choiceTFn' + '\n'
                '{' + str(ans_nb) + '}\n'
                '{' + str(ans_th) + '}\n'
                '{' + str(ans_vd) + '}\n'
                '{' + str(ans_vdc) + '}\n'
                r'\loigiai{' + '\n'
                r'\begin{enumEX}[a)]{1}' + '\n'
                r'\item ' + str(loigiai_nb_1) + '\n'
                r'\item ' + str(loigiai_th_1) + '\n'
                r'\item ' + str(loigiai_vd_1) + '\n'
                r'\item ' + str(loigiai_vdc_1) + '\n'
                r'\end{enumEX}}' + '\n'
                r'\end{ex}' + '\n' + r'\end{minipage}' + '\n\n')
            return content

