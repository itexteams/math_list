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


def bt_dang10_p2_b1_c5_ds10(self):
            # Khai báo biến
            # Ở đây giữ nguyên 3 nữ và 4 nam như đề bài, có thể thay đổi m, n để tạo bài toán mới
            m = 3  # Số học sinh nữ
            n = 4  # Số học sinh nam
            tong = m + n

            # Các giá trị tính toán
            gt_tong = math.factorial(tong) # (a)
            gt_cung_gioi = 2 * math.factorial(m) * math.factorial(n) # (b)
            # (c) Xen kẽ: vì |n-m|=1 nên chỉ có 1 sơ đồ (Nam-Nữ-Nam...)
            gt_xen_ke = math.factorial(m) * math.factorial(n) 
            gt_nu_canh_nhau = math.factorial(n + 1) * math.factorial(m) # (d)

            # Nội dung câu hỏi
            noidungcauhoi = ('''Có %s học sinh nữ và %s học sinh nam cùng xếp theo một hàng ngang.''' 
                             %(latex(m), latex(n)))

            ########################################################################
            # Nhận biết - Câu (a): Tổng số cách xếp
            ########################################################################
            nb_da_1_d = '\\True Có %s cách xếp hàng tùy ý %s học sinh' %(latex(gt_tong), latex(tong))
            nb_da_1_s = 'Có %s cách xếp hàng tùy ý %s học sinh' %(latex(gt_tong + 120), latex(tong))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]

            loigiai_nb_1 = ('''Mỗi cách xếp %s học sinh vào một hàng ngang là một hoán vị của %s phần tử. \\\\
                            Số cách xếp là $P_{%s} = %s! = %s$.'''
                            %(latex(tong), latex(tong), latex(tong), latex(tong), latex(gt_tong)))
            list_nb_2 = [loigiai_nb_1]

            ########################################################################
            # Thông hiểu - Câu (b): Cùng giới đứng cạnh nhau
            ########################################################################
            th_da_1_d = '\\True Có %s cách xếp hàng để học sinh cùng giới đứng cạnh nhau' %(latex(gt_cung_gioi))
            th_da_1_s = 'Có 208 cách xếp hàng để học sinh cùng giới đứng cạnh nhau'
            list_th_da_1 = [th_da_1_d, th_da_1_s]

            loigiai_th_1 = ('''Buộc %s học sinh nữ thành nhóm $A$, %s học sinh nam thành nhóm $B$. \\\\
                            Xếp 2 nhóm $A, B$ có $2!$ cách. \\\\
                            Hoán vị %s nữ trong nội bộ nhóm $A$ có $%s!$ cách. \\\\
                            Hoán vị %s nam trong nội bộ nhóm $B$ có $%s!$ cách. \\\\
                            Vậy có $2! \\cdot %s! \\cdot %s! = %s$ cách.'''
                            %(latex(m), latex(n), latex(m), latex(m), latex(n), latex(n), latex(m), latex(n), latex(gt_cung_gioi)))
            list_th_2 = [loigiai_th_1]

            ########################################################################
            # Vận dụng - Câu (c): Xếp xen kẽ
            ########################################################################
            vd_da_1_d = '\\True Có %s cách xếp hàng để học sinh nam và nữ xếp xen kẽ' %(latex(gt_xen_ke))
            vd_da_1_s = 'Có %s cách xếp hàng để học sinh nam và nữ xếp xen kẽ' %(latex(gt_xen_ke + 20))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]

            loigiai_vd_1 = ('''Vì có %s nam và %s nữ nên để xếp xen kẽ, vị trí các học sinh phải là: Nam-Nữ-Nam-Nữ-Nam-Nữ-Nam. \\\\
                            Xếp %s học sinh nam vào 4 vị trí cố định có $%s!$ cách. \\\\
                            Xếp %s học sinh nữ vào 3 vị trí cố định có $%s!$ cách. \\\\
                            Số cách xếp là $%s! \\cdot %s! = %s$ cách.'''
                            %(latex(n), latex(m), latex(n), latex(n), latex(m), latex(m), latex(n), latex(m), latex(gt_xen_ke)))
            list_vd_2 = [loigiai_vd_1]

            ########################################################################
            # Vận dụng cao - Câu (d): Nữ đứng cạnh nhau
            ########################################################################
            vdc_da_1_d = '\\True Có %s cách xếp hàng để học sinh nữ đứng cạnh nhau' %(latex(gt_nu_canh_nhau))
            vdc_da_1_s = 'Có 700 cách xếp hàng để học sinh nữ đứng cạnh nhau'
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]

            loigiai_vdc_1 = ('''Coi %s học sinh nữ là một nhóm $X$. \\\\
                            Xếp nhóm $X$ và %s học sinh nam (tổng cộng 5 thực thể) có $5!$ cách. \\\\
                            Hoán vị nội bộ %s học sinh nữ có $%s!$ cách. \\\\
                            Số cách xếp là $5! \\cdot %s! = %s$ cách.'''
                            %(latex(m), latex(n), latex(m), latex(m), latex(m), latex(gt_nu_canh_nhau)))
            list_vdc_2 = [loigiai_vdc_1]

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Lặp đến khi có từ 1 đến 3 đáp án đúng
            while True:
                nb_da_1 = random.choice(list_nb_da_1)
                th_da_1 = random.choice(list_th_da_1)
                vd_da_1 = random.choice(list_vd_da_1)
                vdc_da_1 = random.choice(list_vdc_da_1)

                answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
                true_count = count_true_answers(answers)

                if 1 <= true_count <= 3:
                    break

            # Cấu trúc xuất nội dung
            shuffled_solutions = [loigiai_nb_1, loigiai_th_1, loigiai_vd_1, loigiai_vdc_1]

            content = ('\\begin{minipage}{\\textwidth} \n'
                '\\begin{ex}\n'+
                str(noidungcauhoi)+ 
                '\n\\choiceTFn \n'
                '{'+str(nb_da_1)+'}\n'
                '{'+str(th_da_1)+'}\n'
                '{'+str(vd_da_1)+'}\n'
                '{'+str(vdc_da_1)+'}\n'
                '\\loigiai{ \n'
                '\\begin{enumEX}[a)]{1} \n'
                '\\item '+str(shuffled_solutions[0])+'\n'
                '\\item '+str(shuffled_solutions[1])+'\n'
                '\\item '+str(shuffled_solutions[2])+'\n'
                '\\item '+str(shuffled_solutions[3])+'\n'
                '\\end{enumEX}} \n'
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

