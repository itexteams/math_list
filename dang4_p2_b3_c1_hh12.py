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


def bt_dang4_p2_b3_c1_hh12(self):
    # Khai báo biến
    xa = randint(1, 9)
    ya = randint(1, 9)
    za = 0

    xb = randint(-9, 9)
    yb = randint(-9, 9)
    zb = randint(-9, 9)

    xc = randint(1, 9)
    yc = randint(-9, -1)
    zc = za

    xd = randint(-9, -1)
    yd = randint(-9, -1)
    zd = za

    # Trọng tâm tam giác ABC
    xg = Rational(xa + xb + xc, 3)
    yg = Rational(ya + yb + yc, 3)
    zg = Rational(za + zb + zc, 3)

    # Tính góc giữa AB và CD
    xab = xb - xa
    yab = yb - ya
    zab = zb - za
    ab = sqrt(xab**2 + yab**2 + zab**2)

    xcd = xd - xc
    ycd = yd - yc
    zcd = zd - zc
    cd = sqrt(xcd**2 + ycd**2 + zcd**2)

    tich = xab * xcd + yab * ycd + zab * zcd

    cos_goc = tich / (ab * cd)
    goc_rad = math.acos(float(cos_goc))
    goc_do = goc_rad * 180 / math.pi
    goc = Decimal(str(goc_do)).quantize(Decimal('1'), rounding=ROUND_HALF_UP)

    # Tạo hệ số sao cho tổng a + b + c + d != 0
    lis1 = [2, 3, 4, 5, 6, 7, 8, 9, -2, -3, -4, -5, -6, -7, -8, -9]
    while True:
        a = random.choice(lis1)
        b = random.choice(lis1)
        c = random.choice(lis1)
        d = random.choice(lis1)
        tong_hs = a + b + c + d
        if tong_hs != 0:
            break

    # Tọa độ điểm E tính chính xác theo tâm tỉ cự
    xe = Rational(a * xa + b * xb + c * xc + d * xd, tong_hs)
    ye = Rational(a * ya + b * yb + c * yc + d * yd, tong_hs)
    ze = Rational(a * za + b * zb + c * zc + d * zd, tong_hs)

    x = symbols('x')
    y = symbols('y')
    z = symbols('z')

    xae = x - xa
    yae = y - ya
    zae = z - za

    xbe = x - xb
    ybe = y - yb
    zbe = z - zb

    xce = x - xc
    yce = y - yc
    zce = z - zc

    xde = x - xd
    yde = y - yd
    zde = z - zd

    # Tìm trực tâm H của tam giác ACD trong Oxy (z = 0)
    x0 = symbols('x_0')
    y0 = symbols('y_0')
    z0 = 0

    xah = x0 - xa
    yah = y0 - ya
    zah = 0

    xch = x0 - xc
    ych = y0 - yc
    zch = 0

    xad = xd - xa
    yad = yd - ya
    zad = zd - za

    xac = xc - xa
    yac = yc - ya
    zac = zc - za

    # Hệ phương trình trực tâm trong mp Oxy: AH vuông CD và CH vuông AD
    pt1 = xcd * xah + ycd * yah
    pt2 = xad * xch + yad * ych

    he_h = sp.solve((sp.Eq(pt1, 0), sp.Eq(pt2, 0)), (x0, y0))
    xh = he_h[x0]
    yh = he_h[y0]
    zh = 0

    m = random.choice(lis1)
    n = random.choice(lis1)
    p = random.choice(lis1)

    kq = m * xh + n * yh + p * zh

    # Nội dung câu hỏi
    noidungcauhoi = (
        'Trong không gian $Oxyz$, cho bốn điểm $A(%s; %s ;%s), B(%s; %s ;%s), C(%s; %s ;%s)$ và $D(%s; %s ;%s)$.'
        % (
            latex(xa), latex(ya), latex(za),
            latex(xb), latex(yb), latex(zb),
            latex(xc), latex(yc), latex(zc),
            latex(xd), latex(yd), latex(zd),
        )
    )

    ################################ Nhận biết ################################
    nb_da_1_d = '\\True Trọng tâm của tam giác $ABC$ là điểm $G\\left(%s; %s; %s \\right)$' % (latex(xg), latex(yg), latex(zg))
    nb_da_1_s = 'Trọng tâm của tam giác $ABC$ là điểm $G\\left(%s; %s; %s \\right)$' % (latex(xg), latex(yg), latex(zg + 1))
    list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
    nb_da_1 = random.choice(list_nb_da_1)

    loigiai_nb_1 = ('$G$ là trọng tâm tam giác $ABC$ nên $G\\left(%s; %s; %s \\right)$.' % (latex(xg), latex(yg), latex(zg)))

    ################################ Thông hiểu ################################
    th_da_1_d = '\\True Góc giữa hai vectơ $\\vec{AB}$ và $\\vec{CD}$ xấp xỉ bằng $%s^\\circ$' % (latex(goc))
    th_da_1_s = 'Góc giữa hai vectơ $\\vec{AB}$ và $\\vec{CD}$ xấp xỉ bằng $%s^\\circ$' % (latex(goc + 1))
    list_th_da_1 = [th_da_1_d, th_da_1_s]
    th_da_1 = random.choice(list_th_da_1)

    loigiai_th_1 = (
        'Ta có \\\\ \n'
        '\\hspace*{1cm} $\\vec{AB}=(%s; %s; %s) \\Rightarrow \\left| \\vec{AB} \\right|=%s$. \\\\ \n'
        '\\hspace*{1cm} $\\vec{CD}=(%s; %s; %s) \\Rightarrow \\left| \\vec{CD} \\right|=%s$. \\\\ \n'
        '\\hspace*{1cm} $\\vec{AB} \\cdot \\vec{CD}=%s+%s+%s=%s$. \\\\ \n'
        'Khi đó \\\\ \n'
        '\\hspace*{1cm} $\\cos \\left( \\vec{AB}, \\vec{CD} \\right)=\\dfrac{\\vec{AB} \\cdot \\vec{CD}}{\\left| \\vec{AB} \\right| \\cdot \\left| \\vec{CD} \\right|}=\\dfrac{%s}{%s \\cdot %s}=%s$. \\\\ \n'
        'Suy ra góc giữa hai vectơ $\\vec{AB}$ và $\\vec{CD}$ xấp xỉ bằng $%s^\\circ$.'
        % (
            latex(xab), latex(yab), latex(zab), latex(ab),
            latex(xcd), latex(ycd), latex(zcd), latex(cd),
            latex(xab * xcd), latex(yab * ycd), latex(zab * zcd), latex(tich),
            latex(tich), latex(ab), latex(cd), latex(cos_goc),
            latex(goc)
        )
    )

    ################################ Vận dụng ################################
    vd_da_1_d = '\\True Điểm $E$ thỏa mãn $%s\\vec{AE}+%s\\vec{BE}+%s\\vec{CE}+%s\\vec{DE}=\\vec{0}$ khi $E \\left(%s; %s; %s \\right)$' % (
        latex(a), latex(b), latex(c), latex(d), latex(xe), latex(ye), latex(ze)
    )
    vd_da_1_s = 'Điểm $E$ thỏa mãn $%s\\vec{AE}+%s\\vec{BE}+%s\\vec{CE}+%s\\vec{DE}=\\vec{0}$ khi $E \\left(%s; %s; %s \\right)$' % (
        latex(a), latex(b), latex(c), latex(d), latex(xe), latex(ye), latex(ze + 1)
    )
    list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
    vd_da_1 = random.choice(list_vd_da_1)

    loigiai_vd_1 = (
        'Gọi tọa độ điểm $E$ là $(x; y; z)$, ta có \\\\ \n'
        '\\hspace*{1cm} $\\vec{AE}=(%s; %s; %s) \\Rightarrow %s \\vec{AE}=(%s; %s; %s)$. \\\\ \n'
        '\\hspace*{1cm} $\\vec{BE}=(%s; %s; %s) \\Rightarrow %s \\vec{BE}=(%s; %s; %s)$. \\\\ \n'
        '\\hspace*{1cm} $\\vec{CE}=(%s; %s; %s) \\Rightarrow %s \\vec{CE}=(%s; %s; %s)$. \\\\ \n'
        '\\hspace*{1cm} $\\vec{DE}=(%s; %s; %s) \\Rightarrow %s \\vec{DE}=(%s; %s; %s)$. \\\\ \n'
        'Suy ra \\\\ \n'
        '\\hspace*{1cm} $%s\\vec{AE}+%s\\vec{BE}+%s\\vec{CE}+%s\\vec{DE}=(%s; %s; %s)$. \\\\ \n'
        '\\hspace*{1cm} $%s\\vec{AE}+%s\\vec{BE}+%s\\vec{CE}+%s\\vec{DE}=\\vec{0} \\Leftrightarrow \\heva{& %s=0\\\\ & %s=0\\\\& %s=0} \\Leftrightarrow \\heva{& x=%s\\\\ & y=%s\\\\& z=%s.}$ \\\\ \n'
        'Suy ra $E \\left(%s; %s; %s \\right)$.'
        % (
            latex(xae), latex(yae), latex(zae), latex(a), latex(a * xae), latex(a * yae), latex(a * zae),
            latex(xbe), latex(ybe), latex(zbe), latex(b), latex(b * xbe), latex(b * ybe), latex(b * zbe),
            latex(xce), latex(yce), latex(zce), latex(c), latex(c * xce), latex(c * yce), latex(c * zce),
            latex(xde), latex(yde), latex(zde), latex(d), latex(d * xde), latex(d * yde), latex(d * zde),
            latex(a), latex(b), latex(c), latex(d),
            latex(a * xae + b * xbe + c * xce + d * xde), latex(a * yae + b * ybe + c * yce + d * yde), latex(a * zae + b * zbe + c * zce + d * zde),
            latex(a), latex(b), latex(c), latex(d),
            latex(a * xae + b * xbe + c * xce + d * xde), latex(a * yae + b * ybe + c * yce + d * yde), latex(a * zae + b * zbe + c * zce + d * zde),
            latex(xe), latex(ye), latex(ze),
            latex(xe), latex(ye), latex(ze),
        )
    )

    ################################ Vận dụng cao ################################
    vdc_da_1_d = '\\True Gọi $H(x_0; y_0; z_0)$ là trực tâm của tam giác $ACD$ thì $%s x_0+%s y_0+%s z_0=%s$' % (
        latex(m), latex(n), latex(p), latex(kq)
    )
    vdc_da_1_s = 'Gọi $H(x_0; y_0; z_0)$ là trực tâm của tam giác $ACD$ thì $%s x_0+%s y_0+%s z_0=%s$' % (
        latex(m), latex(n), latex(p), latex(kq + 1)
    )
    list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
    vdc_da_1 = random.choice(list_vdc_da_1)

    loigiai_vdc_1 = (
        '$H$ là trực tâm của tam giác $ACD$ và $A, C, D$ cùng thuộc mặt phẳng $(Oxy)$ nên $z_0=0$. \\\\ \n'
        '\\hspace*{1cm} $\\heva{& AH \\bot CD\\\\ & CH \\bot AD}$ nên $\\heva{& \\vec{AH} \\cdot \\vec{CD} =0 \\\\ & \\vec{CH} \\cdot \\vec{AD}=0}$ \\hspace*{1cm} (*). \\\\ \n'
        'Ta có \\\\ \n'
        '\\hspace*{1cm} $\\vec{AH}=(x_0-%s; y_0-%s; 0), \\vec{CD}=(%s; %s; %s)$. \\\\ \n'
        '\\hspace*{1cm} $\\vec{CH}=(x_0-%s; y_0-%s; 0), \\vec{AD}=(%s; %s; %s)$. \\\\ \n'
        'Khi đó (*) $\\Leftrightarrow \\heva{& %s=0\\\\ & %s=0} \\Leftrightarrow \\heva{& x_0=%s\\\\ & y_0=%s.}$ \\\\ \n'
        'Vậy $H \\left(%s; %s; %s \\right)$ nên $%s x_0+%s y_0+%s z_0=%s$.'
        % (
            latex(xa), latex(ya), latex(xcd), latex(ycd), latex(zcd),
            latex(xc), latex(yc), latex(xad), latex(yad), latex(zad),
            latex(pt1), latex(pt2),
            latex(xh), latex(yh),
            latex(xh), latex(yh), latex(zh),
            latex(m), latex(n), latex(p), latex(kq)
        )
    )

    # Lọc đảm bảo có từ 1 đến 3 câu đúng
    def count_true_answers(answers):
        return sum('\\True' in ans for ans in answers)

    while True:
        c_nb = random.choice(list_nb_da_1)
        c_th = random.choice(list_th_da_1)
        c_vd = random.choice(list_vd_da_1)
        c_vdc = random.choice(list_vdc_da_1)
        if 1 <= count_true_answers([c_nb, c_th, c_vd, c_vdc]) <= 3:
            break

    # Kết hợp và xáo trộn
    shuffled_answers_nb, shuffled_solutions_nb = [c_nb], [loigiai_nb_1]
    shuffled_answers_th, shuffled_solutions_th = [c_th], [loigiai_th_1]
    shuffled_answers_vd, shuffled_solutions_vd = [c_vd], [loigiai_vd_1]
    shuffled_answers_vdc, shuffled_solutions_vdc = [c_vdc], [loigiai_vdc_1]

    # Xuất câu hỏi
    content = (
        '\\begin{minipage}{\\textwidth} \n'
        '\\begin{ex}\n' + str(noidungcauhoi) + '\n'
        '\\choiceTFn \n'
        '{' + str(shuffled_answers_nb[0]) + '}\n'
        '{' + str(shuffled_answers_th[0]) + '}\n'
        '{' + str(shuffled_answers_vd[0]) + '}\n'
        '{' + str(shuffled_answers_vdc[0]) + '}\n'
        '\\loigiai{ \n'
        '\\begin{enumEX}[a)]{1} \n'
        '\\item ' + str(shuffled_solutions_nb[0]) + '\n'
        '\\item ' + str(shuffled_solutions_th[0]) + '\n'
        '\\item ' + str(shuffled_solutions_vd[0]) + '\n'
        '\\item ' + str(shuffled_solutions_vdc[0]) + '\n'
        '\\end{enumEX}} \n'
        '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('+-', '-').replace('\\left[', '').replace('\\right]', '')

    return content

