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


def bt_dang30_p2_b1_c1_ds11(self):
            # Khai báo biến
            # B3-Suy nghĩ tìm cách random bài toán
            # Câu a: Random bán kính r_a và số đo góc g_a sao cho rút gọn đẹp
            r_a = random.choice([12, 15, 18, 24])
            g_a = random.choice([40, 50, 60, 75])
            val_l_a = Rational(r_a * g_a, 180)

            # Câu b: Treo tường, kim giờ dài r_b cm (thập phân)
            r_b = random.choice([10.57, 12.34, 15.68])
            r_b_str = str(r_b).replace('.', ',')
            # Tính giá trị cung thực tế với góc quay của kim giờ trong 30 phút là 15 độ (15 * pi / 180 = pi / 12)
            val_l_b = round(r_b * math.pi / 12, 2)
            val_l_b_str = str(val_l_b).replace('.', ',')
            val_l_b_sai_str = str(round(val_l_b + 1.25, 2)).replace('.', ',')

            # Câu c: Bánh xe có N răng, di chuyển m răng
            N_c = random.choice([60, 72, 90])
            m_c = random.choice([10, 12, 15])
            goc_c_correct = int((m_c / N_c) * 360)
            goc_c_sai = goc_c_correct + 10

            # Câu d: Bánh xe đạp bán kính r_d cm, quay k vòng
            r_d = random.choice([40, 50, 60])
            k_d = random.choice([4, 5, 6])
            val_d_correct = k_d * 2 * r_d  # quãng đường = k * 2 * pi * r_d
            val_d_sai = k_d * r_d # thiếu hệ số 2 của đường kính giống mẫu gốc

            # Nội dung câu hỏi theo cấu trúc mẫu dùng định dạng %s
            noidungcauhoi = ('''Các khẳng định sau đúng hay sai?''')

            ########################################################################
            # Nhận biết ############################################
            # Câu a
            nb_da_1_d = '\\True Trên đường tròn bán kính $r = %s$, độ dài của cung có số đo $\\alpha = %s^\\circ$ là $\\frac{%s\\pi}{%s}$' %(r_a, g_a, latex(val_l_a.p), latex(val_l_a.q))
            nb_da_1_s = 'Trên đường tròn bán kính $r = %s$, độ dài của cung có số đo $\\alpha = %s^\\circ$ là $\\frac{%s\\pi}{%s}$' %(r_a, g_a, latex(val_l_a.p + 1), latex(val_l_a.q))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            list_nb_1 = [nb_da_1]

            loigiai_nb_1 = ('''Công thức tính độ dài cung tròn là $l = \\frac{\\pi \\cdot r \\cdot \\alpha}{180}$.\\\\
            Thay số ta được: $l = \\frac{\\pi \\cdot %s \\cdot %s}{180} = \\frac{%s\\pi}{%s}$.''' %(r_a, g_a, latex(val_l_a.p), latex(val_l_a.q)))
            list_nb_2 = [loigiai_nb_1]

            combined_nb = list(zip(list_nb_1, list_nb_2))
            random.shuffle(combined_nb)
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ########################################################################
            # Thông hiểu ############################################
            # Câu b
            th_da_1_d = '\\True Một đồng hồ treo tường, kim giờ dài $%s\\text{ cm}$. Trong $30$ phút, mũi kim giờ vạch lên cung tròn có độ dài gần với $%s\\text{ cm}$' %(r_b_str, val_l_b_str)
            th_da_1_s = 'Một đồng hồ treo tường, kim giờ dài $%s\\text{ cm}$. Trong $30$ phút, mũi kim giờ vạch lên cung tròn có độ dài gần với $%s\\text{ cm}$' %(r_b_str, val_l_b_sai_str)
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            list_th_1 = [th_da_1]

            loigiai_th_1 = ('''Trong $12$ giờ ($720$ phút), kim giờ vạch được một vòng tương ứng $360^\\circ$.\\\\
            Do đó trong $30$ phút, kim giờ vạch được một góc: $\\alpha = \\frac{30}{720} \\cdot 360^\\circ = 15^\\circ$.\\\\
            Độ dài cung tròn mũi kim giờ vạch được là: $l = \\frac{\\pi \\cdot %s \\cdot 15}{180} \\approx %s\\text{ cm}$.''' %(r_b_str, val_l_b_str))
            list_th_2 = [loigiai_th_1]

            combined_th = list(zip(list_th_1, list_th_2))
            random.shuffle(combined_th)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ######################################################################## 
            # Vận dụng ############################################
            # Câu c
            vd_da_1_d = '\\True Một bánh xe có $%s$ răng. Số đo góc mà bánh xe đã quay được khi di chuyển $%s$ răng là $%s^\\circ$' %(N_c, m_c, goc_c_correct)
            vd_da_1_s = 'Một bánh xe có $%s$ răng. Số đo góc mà bánh xe đã quay được khi di chuyển $%s$ răng là $%s^\\circ$' %(N_c, m_c, goc_c_sai)
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            list_vd_1 = [vd_da_1]

            loigiai_vd_1 = ('''Bánh xe có $%s$ răng, khi di chuyển $1$ răng thì bánh xe quay được một góc là: $\\frac{360^\\circ}{%s}$.\\\\
            Khi di chuyển $%s$ răng thì số đo góc quay được là: $\\frac{360^\\circ}{%s} \\cdot %s = %s^\\circ$.''' %(N_c, N_c, m_c, N_c, m_c, goc_c_correct))
            list_vd_2 = [loigiai_vd_1]

            combined_vd = list(zip(list_vd_1, list_vd_2))
            random.shuffle(combined_vd)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ######################################################################## 
            # Vận dụng cao ############################################
            # Câu d (Mẫu gốc: Khẳng định Sai do tính sai công thức chu vi)
            vdc_da_1_s = 'Bánh xe đạp có bán kính $%s\\text{ cm}$. Một người quay bánh xe $%s$ vòng quanh trục thì quãng đường đi được là $%s\\pi\\text{ (cm)}$' %(r_d, k_d, val_d_sai)
            vdc_da_1_d = '\\True Bánh xe đạp có bán kính $%s\\text{ cm}$. Một người quay bánh xe $%s$ vòng quanh trục thì quãng đường đi được là $%s\\pi\\text{ (cm)}$' %(r_d, k_d, val_d_correct)
            list_vdc_da_1 = [vdc_da_1_s, vdc_da_1_d]
            vdc_da_1 = random.choice(list_vdc_da_1)

            list_vdc_1 = [vdc_da_1]

            loigiai_vdc_1 = ('''Chu vi của bánh xe đạp là: $C = 2\\pi \\cdot r = 2\\pi \\cdot %s = %s\\pi\\text{ cm}$.\\\\
            Khi bánh xe quay $%s$ vòng quanh trục thì quãng đường đi được là: $s = %s \\cdot %s\\pi = %s\\pi\\text{ cm}$.''' %(r_d, 2*r_d, k_d, k_d, 2*r_d, val_d_correct))
            list_vdc_2 = [loigiai_vdc_1]

            combined_vdc = list(zip(list_vdc_1, list_vdc_2))
            random.shuffle(combined_vdc)
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

            def count_true_answers(answers):
                return sum('\\True' in ans for ans in answers)

            # Lặp đến khi đáp án có từ 1 đến 3 đúng để bảo toàn logic trắc nghiệm Đúng/Sai
            while True:
                nb_da_1 = random.choice(list_nb_da_1)
                th_da_1 = random.choice(list_th_da_1)
                vd_da_1 = random.choice(list_vd_da_1)
                vdc_da_1 = random.choice(list_vdc_da_1)

                answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
                true_count = count_true_answers(answers)

                if 1 <= true_count <= 3:
                    break

            # Gán lại vào list sau khi lọc điều kiện số câu đúng hợp lệ
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

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn theo đúng định dạng chuỗi %s
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
                '\\end{ex}\n \\end{minipage} \n\n')
            return content

