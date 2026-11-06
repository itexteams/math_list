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


def bt_dang6_p2_b3_c4_ds10(self):
            # Khai báo biến
            # Khai báo biến
            n = symbols('n')

            # B3: Suy nghĩ cách random
            # Ta muốn n1, n2 là hai nghiệm nguyên dương của phương trình lợi nhuận P(n) = 0
            # Giả sử n1 < n2. Khoảng không lỗ là [n1, n2]
            n1 = randint(20, 40)    # Ví dụ: 30
            n2 = randint(80, 130)   # Ví dụ: 100
            gia_ban = randint(15, 25) * 10 # Ví dụ: 200 (nghìn đồng)

            # Tổng chi phí T = n^2 + b_cp*n + c_cp
            # Doanh thu R = gia_ban * n
            # Lợi nhuận P = R - T = -n^2 + (gia_ban - b_cp)n - c_cp
            # Để có nghiệm n1, n2 thì P = -(n - n1)(n - n2) = -n^2 + (n1 + n2)n - n1*n2
            # Suy ra: gia_ban - b_cp = n1 + n2  => b_cp = gia_ban - (n1 + n2)
            # Và: c_cp = n1 * n2

            b_cp = gia_ban - (n1 + n2)
            c_cp = n1 * n2

            # Biểu thức chi phí T
            bt_T = n**2 + b_cp*n + c_cp

            # Các mốc dùng cho đáp án sai
            n_sai_1 = n1 + 20
            n_sai_2 = n2 + 30

            # Nội dung câu hỏi
            noidungcauhoi = ('''Tổng chi phí $T$ (nghìn đồng) để sản xuất $n$ sản phẩm được cho bởi biểu thức $T = %s$. Giá bán của một sản phẩm là %s nghìn đồng. (Giả sử các sản phẩm sản xuất ra đều được bán hết).''' 
                             %(latex(bt_T), latex(gia_ban)))

            ########################################################################
            # Nhận biết (Khẳng định a)
            nb_da_1_d = '\\True Số sản phẩm được sản xuất phải lớn hơn %s thì sẽ bị lỗ.' % (latex(n2))
            nb_da_1_s = 'Số sản phẩm được sản xuất phải lớn hơn %s thì sẽ không bị lỗ.' % (latex(n2))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

            loigiai_nb_1 = ('''Doanh thu thu được là $R(n) = %s n$. \\\\
                            Lợi nhuận của doanh nghiệp là: $P(n) = R(n) - T = %s n - (%s) = -n^2 + %s n - %s$. \\\\
                            Để bị lỗ thì $P(n) < 0 \\Leftrightarrow -n^2 + %s n - %s < 0 \\Leftrightarrow \\left[ \\begin{aligned} & n > %s \\\\ & n < %s \\end{aligned} \\right.$. \\\\
                            Vậy với $n > %s$ thì doanh nghiệp sẽ bị lỗ.''' 
                            %(latex(gia_ban), latex(gia_ban), latex(bt_T), latex(n1+n2), latex(c_cp), latex(n1+n2), latex(c_cp), latex(n2), latex(n1), latex(n2)))

            ########################################################################
            # Thông hiểu (Khẳng định b)
            th_da_1_d = '\\True Số sản phẩm được sản xuất nằm trong khoảng $(%s; %s)$ thì sẽ không bị lỗ.' % (latex(n1), latex(n2))
            th_da_1_s = 'Số sản phẩm được sản xuất phải lớn hơn %s thì sẽ không bị lỗ.' % (latex(n_sai_1))
            list_th_da_1 = [th_da_1_d, th_da_1_s]

            loigiai_th_1 = ('''Để không bị lỗ thì lợi nhuận $P(n) \\ge 0$. \\\\
                            Ta có $P(n) \\ge 0 \\Leftrightarrow -n^2 + %s n - %s \\ge 0 \\Leftrightarrow %s \\le n \\le %s$. \\\\
                            Nếu khẳng định cho rằng $n > %s$ là không chính xác vì khi $n > %s$ doanh nghiệp vẫn bị lỗ.''' 
                            %(latex(n1+n2), latex(c_cp), latex(n1), latex(n2), latex(n_sai_1), latex(n2)))

            ########################################################################
            # Vận dụng (Khẳng định c)
            vd_da_1_d = '\\True Số sản phẩm được sản xuất trong đoạn $[%s;%s]$ thì sẽ không bị lỗ.' % (latex(n1), latex(n2))
            vd_da_1_s = 'Số sản phẩm được sản xuất trong đoạn $[%s;%s]$ thì sẽ không bị lỗ.' % (latex(n_sai_1), latex(n_sai_2))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

            loigiai_vd_1 = ('''Xét bất phương trình $P(n) \\ge 0 \\Leftrightarrow -n^2 + %s n - %s \\ge 0$. \\\\
                            Tam thức bậc hai có hai nghiệm $n = %s, n = %s$ và hệ số $a = -1 < 0$. \\\\
                            Do đó tập nghiệm của bất phương trình là $n \\in [%s; %s]$. \\\\
                            Vậy khẳng định đoạn $[%s; %s]$ là sai vì chứa các giá trị $n > %s$ (gây lỗ).''' 
                            %(latex(n1+n2), latex(c_cp), latex(n1), latex(n2), latex(n1), latex(n2), latex(n_sai_1), latex(n_sai_2), latex(n2)))

            ########################################################################
            # Vận dụng cao (Khẳng định d)
            vdc_da_1_d = '\\True Để lợi nhuận lớn nhất thì số sản phẩm cần sản xuất là %s.' % (latex((n1+n2)//2))
            vdc_da_1_s = 'Số sản phẩm sản xuất trong đoạn $[%s;%s]$ thì sẽ bị lỗ.' % (latex(n1), latex(n2))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

            loigiai_vdc_1 = ('''Lợi nhuận $P(n) = -n^2 + %s n - %s$ là một hàm số bậc hai có đồ thị là parabol bề lõm quay xuống dưới. \\\\
                            Đỉnh của parabol có hoành độ $n_0 = -\\frac{b}{2a} = -\\frac{%s}{2(-1)} = %s$. \\\\
                            Vậy lợi nhuận đạt tối đa khi sản xuất $%s$ sản phẩm. \\\\
                            Khẳng định sản xuất trong đoạn $[%s; %s]$ bị lỗ là sai vì đây chính là đoạn giúp doanh nghiệp có lãi hoặc hòa vốn.''' 
                            %(latex(n1+n2), latex(c_cp), latex(n1+n2), latex((n1+n2)/2), latex(Rational(n1+n2,2)), latex(n1), latex(n2)))

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

            # Gán lại và xáo trộn như mẫu
            list_nb_2 = [loigiai_nb_1]
            list_th_2 = [loigiai_th_1]
            list_vd_2 = [loigiai_vd_1]
            list_vdc_2 = [loigiai_vdc_1]

            combined_nb = list(zip([nb_da_1], list_nb_2))
            combined_th = list(zip([th_da_1], list_th_2))
            combined_vd = list(zip([vd_da_1], list_vd_2))
            combined_vdc = list(zip([vdc_da_1], list_vdc_2))

            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

            # Xuất nội dung
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

