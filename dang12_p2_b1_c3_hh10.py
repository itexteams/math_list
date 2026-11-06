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


def bt_dang12_p2_b1_c3_hh10(self):
            # Khai báo biến
            # Khai báo biến
            x, y = symbols('x y')

            # Hàm để đảm bảo tọa độ trung điểm là số nguyên cho "đẹp"
            def generate_points():
                while True:
                    xM, yM = random.randint(-5, 5), random.randint(-5, 5)
                    xN, yN = random.randint(-5, 5), random.randint(-5, 5)
                    xP, yP = random.randint(-5, 5), random.randint(-5, 5)
                    # Kiểm tra 3 điểm không thẳng hàng và trung điểm NP là số nguyên
                    if (xN + xP) % 2 == 0 and (yN + yP) % 2 == 0:
                        if (xN-xM)*(yP-yM) != (xP-xM)*(yN-yM):
                            return (xM, yM), (xN, yN), (xP, yP)

            (xM, yM), (xN, yN), (xP, yP) = generate_points()

            # Nội dung câu hỏi
            noidungcauhoi = (r"Trong mặt phẳng $Oxy$, cho tam giác $MNP$ có $M(%s; %s), N(%s; %s)$ và $P(%s; %s)$." 
                             % (xM, yM, xN, yN, xP, yP))

            # --- TÍNH TOÁN CÁC THÔNG SỐ ---

            # 1. Đường thẳng MN (NB)
            vec_MN = (xN - xM, yN - yM)
            n_MN = (-(yN - yM), xN - xM) # Pháp tuyến
            c_MN = -(n_MN[0]*xM + n_MN[1]*yM)
            pt_MN = n_MN[0]*x + n_MN[1]*y + c_MN

            # 2. Đường cao kẻ từ M (TH)
            vec_NP = (xP - xN, yP - yN)
            n_caoM = vec_NP # Pháp tuyến là vec chỉ phương NP
            c_caoM = -(n_caoM[0]*xM + n_caoM[1]*yM)
            pt_caoM = n_caoM[0]*x + n_caoM[1]*y + c_caoM

            # 3. Trung trực NP (VD)
            mid_NP = ((xN + xP)//2, (yN + yP)//2)
            n_trungtruc = vec_NP
            c_trungtruc = -(n_trungtruc[0]*mid_NP[0] + n_trungtruc[1]*mid_NP[1])
            pt_trungtruc = n_trungtruc[0]*x + n_trungtruc[1]*y + c_trungtruc

            # 4. Trung tuyến từ M (VDC)
            vec_MI = (mid_NP[0] - xM, mid_NP[1] - yM)
            n_trungtuyen = (-(mid_NP[1] - yM), mid_NP[0] - xM)
            c_trungtuyen = -(n_trungtuyen[0]*xM + n_trungtuyen[1]*yM)
            pt_trungtuyen = n_trungtuyen[0]*x + n_trungtuyen[1]*y + c_trungtuyen

            # --- PHÂN LOẠI ĐÁP ÁN ---

            # NB: Phương trình đường thẳng MN
            nb_da_1_d = r'\True Phương trình tổng quát của đường thẳng $MN$ là $%s = 0$' % latex(pt_MN)
            nb_da_1_s = r'Phương trình tổng quát của đường thẳng $MN$ là $%s = 0$' % latex(pt_MN + random.randint(1, 3))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)
            loigiai_nb_1 = (r"Ta có $\vec{MN} = (%s; %s) \Rightarrow \vec{n}_{MN} = (%s; %s)$.\\ "
                            r"Phương trình $MN$: $%s(x - %s) + %s(y - %s) = 0 \Leftrightarrow %s = 0$."
                            % (vec_MN[0], vec_MN[1], n_MN[0], n_MN[1], n_MN[0], xM, n_MN[1], yM, latex(pt_MN)))

            # TH: Đường cao từ M
            th_da_1_d = r'\True Phương trình tổng quát của đường cao kẻ từ $M$ là $%s = 0$' % latex(pt_caoM)
            th_da_1_s = r'Phương trình tổng quát của đường cao kẻ từ $M$ là $%s = 0$' % latex(pt_caoM - 5)
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)
            loigiai_th_1 = (r"Đường cao kẻ từ $M$ vuông góc với $NP$ nên nhận $\vec{NP} = (%s; %s)$ làm vectơ pháp tuyến. "
                            r"Phương trình: $%s(x - %s) + %s(y - %s) = 0 \Leftrightarrow %s = 0$."
                            % (vec_NP[0], vec_NP[1], n_caoM[0], xM, n_caoM[1], yM, latex(pt_caoM)))

            # VD: Trung trực NP
            vd_da_1_d = r'\True Phương trình tổng quát của đường trung trực đoạn thẳng $NP$ là $%s = 0$' % latex(pt_trungtruc)
            vd_da_1_s = r'Phương trình tổng quát của đường trung trực đoạn thẳng $NP$ là $%s = 0$' % latex(pt_trungtruc + 2)
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)
            loigiai_vd_1 = (r"Gọi $I$ là trung điểm $NP \Rightarrow I(%s; %s)$. Đường trung trực $NP$ đi qua $I$ và vuông góc với $NP$ "
                            r"nên nhận $\vec{NP} = (%s; %s)$ làm vectơ pháp tuyến. Phương trình: %s = 0."
                            % (mid_NP[0], mid_NP[1], vec_NP[0], vec_NP[1], latex(pt_trungtruc)))

            # VDC: Trung tuyến từ M
            vdc_da_1_d = r'\True Phương trình tổng quát của đường trung tuyến kẻ từ $M$ là $%s = 0$' % latex(pt_trungtuyen)
            vdc_da_1_s = r'Phương trình tổng quát của đường trung tuyến kẻ từ $M$ là $%s = 0$' % latex(pt_trungtuyen + x)
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)
            loigiai_vdc_1 = (r"Gọi $I$ là trung điểm $NP \Rightarrow I(%s; %s)$. Đường trung tuyến kẻ từ $M$ đi qua $M(%s; %s)$ và $I(%s; %s)$. "
                             r"Ta có $\vec{MI} = (%s; %s) \Rightarrow \vec{n} = (%s; %s)$. Phương trình: $%s = 0$."
                             % (mid_NP[0], mid_NP[1], xM, yM, mid_NP[0], mid_NP[1], vec_MI[0], vec_MI[1], n_trungtuyen[0], n_trungtuyen[1], latex(pt_trungtuyen)))

            # --- XỬ LÝ RANDOM VÀ XUẤT NỘI DUNG ---

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            while True:
                nb_sel = random.choice(list_nb_da_1)
                th_sel = random.choice(list_th_da_1)
                vd_sel = random.choice(list_vd_da_1)
                vdc_sel = random.choice(list_vdc_da_1)
                if 1 <= count_true_answers([nb_sel, th_sel, vd_sel, vdc_sel]) <= 3:
                    break

            # Gán và trộn (theo cấu trúc mẫu)
            ans_list = [(nb_sel, loigiai_nb_1), (th_sel, loigiai_th_1), (vd_sel, loigiai_vd_1), (vdc_sel, loigiai_vdc_1)]
            # Lưu ý: Giữ nguyên thứ tự a, b, c, d tương ứng NB, TH, VD, VDC để khớp lời giải
            final_ans = [x[0] for x in ans_list]
            final_sol = [x[1] for x in ans_list]

            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n' +
                str(noidungcauhoi) + '\n' +
                '\\choiceTFn \n'
                '{' + str(final_ans[0]) + '}\n'
                '{' + str(final_ans[1]) + '}\n'
                '{' + str(final_ans[2]) + '}\n'
                '{' + str(final_ans[3]) + '}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item ' + str(final_sol[0]) + '\n'
                '\\item ' + str(final_sol[1]) + '\n'
                '\\item ' + str(final_sol[2]) + '\n'
                '\\item ' + str(final_sol[3]) + '\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n').replace('+-','-').replace('+ -','-')
            return content   

