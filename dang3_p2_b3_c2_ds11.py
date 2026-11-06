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


def bt_dang3_p2_b3_c2_ds11(self):
            # Khai báo biến
            lisdang=['1','2']
            dang=random.choice(lisdang)
            if dang =='2':
                lisu1=[2,3,-2,-3,4,-4]
                u1=random.choice(lisu1)

                lisq=[-2,-3,-Rational(1,2),-Rational(1,3),-4,-Rational(1,4)]
                q=random.choice(lisq)

                lisn=[2,3,4,5,6,7]
                n=random.choice(lisn)
                un=u1*q**(n-1)

                lisn.remove(n)
                n1=random.choice(lisn)
                sn1=u1*Rational(q**n1-1,q-1)

                lisn.remove(n1)
                n2=random.choice(lisn)
                un2=u1*q**(n2-1)

                lisn.remove(n2)
                n3=random.choice(lisn)
                sn3=u1*Rational(q**n3-1,q-1)

                lisn.remove(n3)
                n4=random.choice(lisn)
                un4=u1*q**(n4-1)

                # Nội dung câu hỏi
                noidungcauhoi = 'Cho cấp số nhân $(u_n)$ có công bội âm. Biết $u_%s=%s$ và $u_%s=%s$. \n' %(latex(n),latex(un),latex(n4),latex(un4))

                ######################################################################## Nhận biết ############################################
                # Các đáp án
                nb_da_1_d = '\\True Công bội của cấp số nhân là $q=%s$' %(latex(q))
                nb_da_1_s = 'Công bội của cấp số nhân là $q=%s$' %(latex(q+1))
                list_nb_da_1=[nb_da_1_d,nb_da_1_s]
                nb_da_1=random.choice(list_nb_da_1)

                nb_da_2_d = '\\True Số hạng đầu của cấp số nhân là $u_1=%s$' %(latex(u1))
                nb_da_2_s = 'Số hạng đầu của cấp số nhân là $u_1=%s$' %(latex(u1-1))
                list_nb_da_2=[nb_da_2_d,nb_da_2_s]
                nb_da_2=random.choice(list_nb_da_2)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_nb_1 = [nb_da_1, nb_da_2]

                # Nội dung lời giải
                loigiai_nb_1 = ('Ta có $u_%s=u_1 q^{%s}$ và $u_%s=u_1 q^{%s}$ suy ra $\\dfrac{q^{%s}}{q^{%s}}=\\dfrac{%s}{%s} \\Leftrightarrow q^{%s}=%s \\Leftrightarrow q=%s$.'
                            %( latex(n),latex(n-1),latex(n4),latex(n4-1),latex(n-1),latex(n4-1),latex(un),latex(un4),latex(n-n4),latex(Rational(un,un4)),latex(q)
                            ))
                loigiai_nb_2 = ('Ta có $u_%s=u_1 q^{%s}$ và $u_%s=u_1 q^{%s}$ suy ra $\\dfrac{q^{%s}}{q^{%s}}=\\dfrac{%s}{%s} \\Leftrightarrow q^{%s}=%s \\Leftrightarrow q=%s$. \\\\ \n'
                                'Số hạng đầu của cấp số nhân là $u_1=\\dfrac{u_%s}{q^{%s}}=\\dfrac{%s}{\\left( %s \\right)^%s}=%s$.'
                            %( latex(n),latex(n-1),latex(n4),latex(n4-1),latex(n-1),latex(n4-1),latex(un),latex(un4),latex(n-n4),latex(Rational(un,un4)),latex(q),
                            latex(n),latex(n-1),latex(un),latex(q),latex(n-1),latex(u1)
                            ))

                # Đưa các lời giải vào danh sách lời giải
                list_nb_2 = [loigiai_nb_1,loigiai_nb_2]

                # Kết hợp các đáp án và lời giải vào cùng một danh sách
                combined_nb = list(zip(list_nb_1, list_nb_2))

                # Xáo trộn danh sách kết hợp
                random.shuffle(combined_nb)

                # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
                shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

                ######################################################################## Thông hiểu ############################################
                # Các đáp án
                th_da_1_d = '\\True Tổng $%s$ số hạng đầu của cấp số nhân là $%s$' %(latex(n1),latex(sn1))
                th_da_1_s = 'Tổng $%s$ số hạng đầu của cấp số nhân là $%s$' %(latex(n1),latex(sn1-1))
                list_th_da_1=[th_da_1_d,th_da_1_s]
                th_da_1=random.choice(list_th_da_1)

                # Các đáp án
                th_da_2_d = '\\True Số hạng thứ $%s$ của cấp số nhân là $%s$' %(latex(n),latex(un))
                th_da_2_s = 'Số hạng thứ $%s$ của cấp số nhân là $%s$' %(latex(n),latex(un+1))
                list_th_da_2=[th_da_2_d,th_da_2_s]
                th_da_2=random.choice(list_th_da_2)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_th_1 = [th_da_1,th_da_2]

                # Nội dung lời giải
                loigiai_th_1 = ('Tổng $%s$ số hạng đầu của cấp số nhân là $S_%s=u_1 \\dfrac{q^%s-1}{q-1}=%s \\cdot \\dfrac{\\left(%s\\right)^%s-1}{%s-1}=%s$.'
                                %(latex(n1),latex(n1),latex(n1),
                                latex(u1),latex(q),latex(n1),latex(q),latex(sn1)
                            ))
                loigiai_th_2 = ('Số hạng thứ $%s$ của cấp số nhân là $u_%s=u_1 q^%s=%s \\cdot \\left( %s \\right)^%s=%s$.'
                            %( latex(n),latex(n),latex(n-1),latex(u1), latex(q),latex(n-1),latex(un)
                            ))

                # Đưa các lời giải vào danh sách lời giải
                list_th_2 = [loigiai_th_1,loigiai_th_2]

                # Kết hợp các đáp án và lời giải vào cùng một danh sách
                combined_th = list(zip(list_th_1, list_th_2))

                # Xáo trộn danh sách kết hợp
                random.shuffle(combined_th)

                # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
                shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

                ######################################################################## Vận dụng ############################################
                # Các đáp án
                vd_da_1_d = '\\True Số $%s$ là số hạng thứ $%s$ của cấp số nhân' %(latex(un2),latex(n2))
                vd_da_1_s = 'Số $%s$ là số hạng thứ $%s$ của cấp số nhân' %(latex(un2),latex(n2+1))
                list_vd_da_1=[vd_da_1_d,vd_da_1_s]
                vd_da_1=random.choice(list_vd_da_1)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_vd_1 = [vd_da_1]

                # Nội dung lời giải
                loigiai_vd_1 = ('Gọi $u_n=%s \\Leftrightarrow u_1 q^{n-1}=%s \\Leftrightarrow %s \\cdot \\left(%s\\right)^{n-1}=%s \\Leftrightarrow \\left(%s\\right)^{n-1}=%s \\Leftrightarrow n=%s$. \\\\ \n'
                                'Do đó, số $%s$ là số hạng thứ $%s$ của cấp số nhân.'
                                %(latex(un2),latex(un2),
                                latex(u1),latex(q),latex(un2),
                                latex(q),latex(Rational(un2,u1)),
                                latex(n2),
                                latex(un2),latex(n2)
                            ))

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
                vdc_da_1_d = '\\True Số $%s$ là tổng của $%s$ số hạng đầu của cấp số nhân' %(latex(sn3),latex(n3))
                vdc_da_1_s = 'Số $%s$ là tổng của $%s$ số hạng đầu của cấp số nhân' %(latex(sn3),latex(n3-1))
                list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
                vdc_da_1=random.choice(list_vdc_da_1)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_vdc_1 = [vdc_da_1]

                # Nội dung lời giải
                loigiai_vdc_1 = ('Gọi $S_n=%s \\Leftrightarrow u_1 \\dfrac{q^n-1}{q-1}=%s \\Leftrightarrow %s \\cdot \\dfrac{\\left(%s\\right)^n-1}{%s-1}=%s$ \\\\ \n' 
                                '\\hspace*{2.5cm} $\\Leftrightarrow \\left(%s\\right)^n-1=%s \\Leftrightarrow n=%s$. \\\\ \n'
                                'Do đó, số $%s$ là tổng của $%s$ số hạng đầu của cấp số nhân.'
                                %(latex(sn3),latex(sn3),
                                latex(u1),latex(q),latex(q),latex(sn3),
                                latex(q),latex(Rational(sn3*(q-1),u1)),latex(n3),
                                latex(sn3),latex(n3)
                            ))

                # Đưa các lời giải vào danh sách lời giải
                list_vdc_2 = [loigiai_vdc_1]

                # Kết hợp các đáp án và lời giải vào cùng một danh sách
                combined_vdc = list(zip(list_vdc_1, list_vdc_2))

                # Xáo trộn danh sách kết hợp
                random.shuffle(combined_vdc)

                # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
                shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)
            if dang =='1':
                lisu1=[2,3,-2,-3,4,-4]
                u1=random.choice(lisu1)

                lisq=[2,3,Rational(1,2),Rational(1,3),4,Rational(1,4)]
                q=random.choice(lisq)

                lisn=[2,3,4,5,6,7]
                n=random.choice(lisn)
                un=u1*q**(n-1)

                lisn.remove(n)
                n1=random.choice(lisn)
                sn1=u1*Rational(q**n1-1,q-1)

                lisn.remove(n1)
                n2=random.choice(lisn)
                un2=u1*q**(n2-1)

                lisn.remove(n2)
                n3=random.choice(lisn)
                sn3=u1*Rational(q**n3-1,q-1)

                lisn.remove(n3)
                n4=random.choice(lisn)
                un4=u1*q**(n4-1)

                # Nội dung câu hỏi
                noidungcauhoi = 'Cho cấp số nhân $(u_n)$ có công bội dương. Biết $u_%s=%s$ và $u_%s=%s$. \n' %(latex(n),latex(un),latex(n4),latex(un4))

                ######################################################################## Nhận biết ############################################
                # Các đáp án
                nb_da_1_d = '\\True Công bội của cấp số nhân là $q=%s$' %(latex(q))
                nb_da_1_s = 'Công bội của cấp số nhân là $q=%s$' %(latex(q+1))
                list_nb_da_1=[nb_da_1_d,nb_da_1_s]
                nb_da_1=random.choice(list_nb_da_1)

                nb_da_2_d = '\\True Số hạng đầu của cấp số nhân là $u_1=%s$' %(latex(u1))
                nb_da_2_s = 'Số hạng đầu của cấp số nhân là $u_1=%s$' %(latex(u1-1))
                list_nb_da_2=[nb_da_2_d,nb_da_2_s]
                nb_da_2=random.choice(list_nb_da_2)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_nb_1 = [nb_da_1, nb_da_2]

                # Nội dung lời giải
                loigiai_nb_1 = ('Ta có $u_%s=u_1 q^{%s}$ và $u_%s=u_1 q^{%s}$ suy ra $\\dfrac{q^{%s}}{q^{%s}}=\\dfrac{%s}{%s} \\Leftrightarrow q^{%s}=%s \\Leftrightarrow q=%s$.'
                            %( latex(n),latex(n-1),latex(n4),latex(n4-1),latex(n-1),latex(n4-1),latex(un),latex(un4),latex(n-n4),latex(Rational(un,un4)),latex(q)
                            ))
                loigiai_nb_2 = ('Ta có $u_%s=u_1 q^{%s}$ và $u_%s=u_1 q^{%s}$ suy ra $\\dfrac{q^{%s}}{q^{%s}}=\\dfrac{%s}{%s} \\Leftrightarrow q^{%s}=%s \\Leftrightarrow q=%s$. \\\\ \n'
                                'Số hạng đầu của cấp số nhân là $u_1=\\dfrac{u_%s}{q^{%s}}=\\dfrac{%s}{\\left( %s \\right)^%s}=%s$.'
                            %( latex(n),latex(n-1),latex(n4),latex(n4-1),latex(n-1),latex(n4-1),latex(un),latex(un4),latex(n-n4),latex(Rational(un,un4)),latex(q),
                            latex(n),latex(n-1),latex(un),latex(q),latex(n-1),latex(u1)
                            ))

                # Đưa các lời giải vào danh sách lời giải
                list_nb_2 = [loigiai_nb_1,loigiai_nb_2]

                # Kết hợp các đáp án và lời giải vào cùng một danh sách
                combined_nb = list(zip(list_nb_1, list_nb_2))

                # Xáo trộn danh sách kết hợp
                random.shuffle(combined_nb)

                # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
                shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

                ######################################################################## Thông hiểu ############################################
                # Các đáp án
                th_da_1_d = '\\True Tổng $%s$ số hạng đầu của cấp số nhân là $%s$' %(latex(n1),latex(sn1))
                th_da_1_s = 'Tổng $%s$ số hạng đầu của cấp số nhân là $%s$' %(latex(n1),latex(sn1-1))
                list_th_da_1=[th_da_1_d,th_da_1_s]
                th_da_1=random.choice(list_th_da_1)

                # Các đáp án
                th_da_2_d = '\\True Số hạng thứ $%s$ của cấp số nhân là $%s$' %(latex(n),latex(un))
                th_da_2_s = 'Số hạng thứ $%s$ của cấp số nhân là $%s$' %(latex(n),latex(un+1))
                list_th_da_2=[th_da_2_d,th_da_2_s]
                th_da_2=random.choice(list_th_da_2)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_th_1 = [th_da_1,th_da_2]

                # Nội dung lời giải
                loigiai_th_1 = ('Tổng $%s$ số hạng đầu của cấp số nhân là $S_%s=u_1 \\dfrac{q^%s-1}{q-1}=%s \\cdot \\dfrac{\\left(%s\\right)^%s-1}{%s-1}=%s$.'
                                %(latex(n1),latex(n1),latex(n1),
                                latex(u1),latex(q),latex(n1),latex(q),latex(sn1)
                            ))
                loigiai_th_2 = ('Số hạng thứ $%s$ của cấp số nhân là $u_%s=u_1 q^%s=%s \\cdot \\left( %s \\right)^%s=%s$.'
                            %( latex(n),latex(n),latex(n-1),latex(u1), latex(q),latex(n-1),latex(un)
                            ))

                # Đưa các lời giải vào danh sách lời giải
                list_th_2 = [loigiai_th_1,loigiai_th_2]

                # Kết hợp các đáp án và lời giải vào cùng một danh sách
                combined_th = list(zip(list_th_1, list_th_2))

                # Xáo trộn danh sách kết hợp
                random.shuffle(combined_th)

                # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
                shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

                ######################################################################## Vận dụng ############################################
                # Các đáp án
                vd_da_1_d = '\\True Số $%s$ là số hạng thứ $%s$ của cấp số nhân' %(latex(un2),latex(n2))
                vd_da_1_s = 'Số $%s$ là số hạng thứ $%s$ của cấp số nhân' %(latex(un2),latex(n2+1))
                list_vd_da_1=[vd_da_1_d,vd_da_1_s]
                vd_da_1=random.choice(list_vd_da_1)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_vd_1 = [vd_da_1]

                # Nội dung lời giải
                loigiai_vd_1 = ('Gọi $u_n=%s \\Leftrightarrow u_1 q^{n-1}=%s \\Leftrightarrow %s \\cdot \\left(%s\\right)^{n-1}=%s \\Leftrightarrow \\left(%s\\right)^{n-1}=%s \\Leftrightarrow n=%s$. \\\\ \n'
                                'Do đó, số $%s$ là số hạng thứ $%s$ của cấp số nhân.'
                                %(latex(un2),latex(un2),
                                latex(u1),latex(q),latex(un2),
                                latex(q),latex(Rational(un2,u1)),
                                latex(n2),
                                latex(un2),latex(n2)
                            ))

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
                vdc_da_1_d = '\\True Số $%s$ là tổng của $%s$ số hạng đầu của cấp số nhân' %(latex(sn3),latex(n3))
                vdc_da_1_s = 'Số $%s$ là tổng của $%s$ số hạng đầu của cấp số nhân' %(latex(sn3),latex(n3-1))
                list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
                vdc_da_1=random.choice(list_vdc_da_1)

                # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
                list_vdc_1 = [vdc_da_1]

                # Nội dung lời giải
                loigiai_vdc_1 = ('Gọi $S_n=%s \\Leftrightarrow u_1 \\dfrac{q^n-1}{q-1}=%s \\Leftrightarrow %s \\cdot \\dfrac{\\left(%s\\right)^n-1}{%s-1}=%s$ \\\\ \n' 
                                '\\hspace*{2.5cm} $\\Leftrightarrow \\left(%s\\right)^n-1=%s \\Leftrightarrow n=%s$. \\\\ \n'
                                'Do đó, số $%s$ là tổng của $%s$ số hạng đầu của cấp số nhân.'
                                %(latex(sn3),latex(sn3),
                                latex(u1),latex(q),latex(q),latex(sn3),
                                latex(q),latex(Rational(sn3*(q-1),u1)),latex(n3),
                                latex(sn3),latex(n3)
                            ))

                # Đưa các lời giải vào danh sách lời giải
                list_vdc_2 = [loigiai_vdc_1]

                # Kết hợp các đáp án và lời giải vào cùng một danh sách
                combined_vdc = list(zip(list_vdc_1, list_vdc_2))

                # Xáo trộn danh sách kết hợp
                random.shuffle(combined_vdc)

                # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
                shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)



            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+ str(noidungcauhoi)+ 
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
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac')
            return content

