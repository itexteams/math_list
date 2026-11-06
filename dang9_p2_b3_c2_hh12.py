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


def bt_dang9_p2_b3_c2_hh12(self):
            # Khai báo biến
            # Định nghĩa các biến ký hiệu nếu cần
            x = symbols('x')


            k = random.choice([1, 2]) # Chọn hệ số tỉ lệ để giữ tọa độ nguyên đẹp
            # Tọa độ các điểm sau khi tỉ lệ hóa và tịnh tiến nhẹ
            xS, yS, zS = 0, 5 * k, 10 * k
            xC, yC, zC = 8 * k, 9 * k, 2 * k
            xD, yD, zD = 16 * k, 7 * k, 0

            # Các hệ số của mặt phẳng (P): x + 2y + 2z - 30k = 0
            A_p, B_p, C_p, D_p = 1, 2, 2, -30 * k

            # Độ dài đại số và các giá trị tính toán theo k
            sc_len = 12 * k
            radius = 6 * k * math.sqrt(2)
            total_dist_real = (12 * k + 3 * math.pi * k) * 5

            # Làm tròn quãng đường thực tế đến hàng đơn vị
            total_dist_round = round(total_dist_real)

            # Nội dung câu hỏi
            noidungcauhoi = ('''Trong không gian với hệ trục $Oxyz$, một vận động viên thực hiện bài thi trượt tuyết trên một sườn dốc phẳng $(P)$ và xuất phát từ vị trí $S(%s;%s;%s)$. Trên sườn dốc, vận động viên trượt theo một đường thẳng từ $S$ đến điểm $C(%s;%s;%s)$. Tại $C$, vận động viên chuyển hướng trượt theo một cung tròn tâm $M$ nằm trong mặt phẳng sườn dốc và đi qua điểm $D(%s;%s;%s)$. Biết đường thẳng $SC$ là tiếp tuyến của cung tròn quỹ đạo tại $C$.''' 
                             % (latex(xS), latex(yS), latex(zS), latex(xC), latex(yC), latex(zC), latex(xD), latex(yD), latex(zD)))

            ########################################################################
            # Nhận biết ############################################
            # Câu a: Phương trình mặt phẳng sườn dốc
            nb_da_1_d = '\\True Phương trình mặt phẳng sườn dốc $(P)$ là $x+2y+2z-%s=0$' % (latex(-D_p))
            nb_da_1_s = 'Phương trình mặt phẳng sườn dốc $(P)$ là $2x+y+2z-%s=0$' % (latex(-D_p))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            list_nb_1 = [nb_da_1]

            loigiai_nb_1 = ('''Mặt phẳng $(P)$ đi qua ba điểm $S(%s;%s;%s), C(%s;%s;%s), D(%s;%s;%s)$.\\\\
            Ta có tọa độ các vectơ: $\\overrightarrow{SC}=(%s;%s;%s)=%s(2;1;-2)$ và $\\overrightarrow{SD}=(%s;%s;%s)=%s(8;1;-5)$.\\\\
            Vectơ pháp tuyến của mặt phẳng $(P)$ là: $\\vec{n}_P=[\\overrightarrow{SC},\\overrightarrow{SD}]=(%s;%s;%s)$.\\\\
            Chọn $\\vec{n}=(1;2;2)$ làm một vectơ pháp tuyến.\\\\
            Phương trình mặt phẳng $(P)$ đi qua $S(%s;%s;%s)$ là:\\\\
            $1(x-%s)+2(y-%s)+2(z-%s)=0 \\Leftrightarrow x+2y+2z-%s=0$.'''
                            % (latex(xS), latex(yS), latex(zS), latex(xC), latex(yC), latex(zC), latex(xD), latex(yD), latex(zD),
                               latex(xC-xS), latex(yC-yS), latex(zC-zS), latex(4*k),
                               latex(xD-xS), latex(yD-yS), latex(zD-zS), latex(2*k),
                               latex(-3*k), latex(-6*k), latex(-6*k),
                               latex(xS), latex(yS), latex(zS),
                               latex(xS), latex(yS), latex(zS), latex(-D_p)))

            list_nb_2 = [loigiai_nb_1]
            combined_nb = list(zip(list_nb_1, list_nb_2))
            random.shuffle(combined_nb)
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ########################################################################
            # Thông hiểu ############################################
            # Câu b: Góc giữa SC và Oxy
            th_da_1_d = 'Gọi $\\alpha$ là góc tạo bởi đường trượt thẳng $SC$ và mặt phẳng nằm ngang $(Oxy)$ thì $\\sin\\alpha=\\frac{1}{3}$'
            th_da_1_s = '\\True Gọi $\\alpha$ là góc tạo bởi đường trượt thẳng $SC$ và mặt phẳng nằm ngang $(Oxy)$ thì $\\sin\\alpha=\\frac{2}{3}$'
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            list_th_1 = [th_da_1]

            loigiai_th_1 = ('''Vectơ chỉ phương của đường thẳng $SC$ là $\\vec{u}_{SC}=(2;1;-2)$.\\\\
            Vectơ pháp tuyến của mặt phẳng $(Oxy)$ là $\\vec{k}=(0;0;1)$.\\\\
            $\\sin\\alpha = \\frac{|\\vec{u}_{SC}\\cdot\\vec{k}|}{|\\vec{u}_{SC}|\\cdot|\\vec{k}|} = \\frac{|-2|}{\\sqrt{2^2+1^2+(-2)^2}\\cdot 1} = \\frac{2}{3}$.''' )

            list_th_2 = [loigiai_th_1]
            combined_th = list(zip(list_th_1, list_th_2))
            random.shuffle(combined_th)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ########################################################################
            # Vận dụng ############################################
            # Câu c: Bán kính đường tròn R
            radius_latex = '6\\sqrt{2}' if k == 1 else '12\\sqrt{2}'
            radius_wrong_latex = '6\\sqrt{2}' if k == 2 else '6'

            vd_da_1_d = 'Bán kính quỹ đạo cung tròn của đoạn rẽ hướng là $R=%s$' % radius_wrong_latex
            vd_da_1_s = '\\True Bán kính quỹ đạo cung tròn của đoạn rẽ hướng là $R=%s$' % radius_latex
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            list_vd_1 = [vd_da_1]

            xM, yM, zM = 12 * k, 5 * k, 4 * k
            loigiai_vd_1 = ('''Cung tròn tâm $M$ nằm trong mặt phẳng $(P)$ đi qua $C, D$ và tiếp xúc $SC$ tại $C$.\\\\
            Gọi $M(x;y;z)$ và do $M \\in (P) \\Rightarrow x+2y+2z=%s \\quad (1)$\\\\
            Mặt khác, ta có $SC$ là tiếp tuyến với cung tròn tại tiếp điểm $C$ nên $MC \\perp SC \\Rightarrow \\overrightarrow{MC}\\cdot\\overrightarrow{SC}=0$.\\\\
            Với $\\overrightarrow{MC}=(%s-x;%s-y;%s-z)$ và $\\overrightarrow{SC}=(%s;%s;%s)$, ta có:\\\\
            $\\overrightarrow{MC}\\cdot\\overrightarrow{SC}=0 \\Leftrightarrow 8( %s-x)+4( %s-y)-8( %s-z)=0 \\Leftrightarrow 2x+y-2z=%s \\quad (2)$\\\\
            Lại có $MC=MD \\Leftrightarrow MC^2=MD^2$ nên khi đó:\\\\
            $(x-%s)^2+(y-%s)^2+(z-%s)^2=(x-%s)^2+(y-%s)^2+z^2 \\Leftrightarrow 4x-y-z=%s \\quad (3)$\\\\
            Giải hệ phương trình từ $(1), (2)$ và $(3)$ ta tìm được tọa độ tâm $M(%s;%s;%s)$.\\\\
            Bán kính $R=MC=\\sqrt{(%s-%s)^2+(%s-%s)^2+(%s-%s)^2}=%s$.''' 
                            % (latex(-D_p), latex(xC), latex(yC), latex(zC), latex(xC-xS), latex(yC-yS), latex(zC-zS),
                               latex(xC), latex(yC), latex(zC), latex(21*k),
                               latex(xC), latex(yC), latex(zC), latex(xD), latex(yD), latex(39*k),
                               latex(xM), latex(yM), latex(zM),
                               latex(xM), latex(xC), latex(yM), latex(yC), latex(zM), latex(zC), radius_latex))

            list_vd_2 = [loigiai_vd_1]
            combined_vd = list(zip(list_vd_1, list_vd_2))
            random.shuffle(combined_vd)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ########################################################################
            # Vận dụng cao ############################################
            # Câu d: Tính tổng quãng đường thực tế
            vdc_da_1_d = '\\True Giả sử mỗi đơn vị độ dài trong hệ tọa độ ứng với $5\\text{ m}$ thực tế. Tổng quãng đường thực tế vận động viên đã đi từ $S$ đến $D$ bằng $%s\\text{ m}$ (Kết quả làm tròn đến hàng đơn vị)' % (latex(total_dist_round))
            vdc_da_1_s = 'Giả sử mỗi đơn vị độ dài trong hệ tọa độ ứng với $5\\text{ m}$ thực tế. Tổng quãng đường thực tế vận động viên đã đi từ $S$ đến $D$ bằng $%s\\text{ m}$ (Kết quả làm tròn đến hàng đơn vị)' % (latex(total_dist_round - 10))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            list_vdc_1 = [vdc_da_1]

            loigiai_vdc_1 = ('''Độ dài đoạn thẳng $SC=\\sqrt{%s^2+%s^2+(%s)^2}=%s$ đơn vị độ dài.\\\\
            Để tính độ dài cung $CD$, ta cần tìm góc $\\varphi = \\widehat{CMD}$.\\\\
            Ta có: $\\overrightarrow{MC}=(%s;%s;%s)$ và $\\overrightarrow{MD}=(%s;%s;%s) \\Rightarrow \\cos\\varphi = \\frac{\\overrightarrow{MC}\\cdot\\overrightarrow{MD}}{|\\overrightarrow{MC}|\\cdot|\\overrightarrow{MD}|} = 0 \\Rightarrow \\varphi = \\frac{\\pi}{2}$.\\\\
            Độ dài cung $L_{\\overset\\frown{CD}} = R\\cdot\\varphi = %s\\cdot\\frac{\\pi}{2} = %s\\pi$ đơn vị độ dài.\\\\
            Quãng đường thực tế là $S = (%s + %s\\pi)\\cdot 5 \\approx %s\\text{ m}$.'''
                             % (latex(xC-xS), latex(yC-yS), latex(zC-zS), latex(sc_len),
                                latex(xC-xM), latex(yC-yM), latex(zC-zM), latex(xD-xM), latex(yD-yM), latex(zD-zM),
                                radius_latex, latex(3*k), latex(sc_len), latex(3*k), latex(total_dist_round)))

            list_vdc_2 = [loigiai_vdc_1]
            combined_vdc = list(zip(list_vdc_1, list_vdc_2))
            random.shuffle(combined_vdc)
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Vòng lặp đảm bảo số lượng đáp án đúng từ 1 đến 3
            while True:
                nb_da_1 = random.choice(list_nb_da_1)
                th_da_1 = random.choice(list_th_da_1)
                vd_da_1 = random.choice(list_vd_da_1)
                vdc_da_1 = random.choice(list_vdc_da_1)

                answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
                true_count = count_true_answers(answers)

                if 1 <= true_count <= 3:
                    break

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
                '\n\\choiceTFn \n'
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

