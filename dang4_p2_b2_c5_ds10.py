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


def bt_dang4_p2_b2_c5_ds10(self):
            # Khai báo biến
            # Số ghế mỗi hàng cố định là 6 để đảm bảo logic 4 hàng (tổng 24 ghế) > số học sinh
            n_students = randint(20, 22)
            k_seats = 6

            # Các mốc học sinh còn lại sau mỗi hàng
            n_con_lai_1 = n_students - k_seats
            n_con_lai_2 = n_con_lai_1 - k_seats
            n_con_lai_3 = n_con_lai_2 - k_seats

            # Nội dung câu hỏi
            noidungcauhoi = ('''Một trường trung học phổ thông có %s bạn học sinh tham dự tọa đàm về tháng Thanh niên do Quận Đoàn tổ chức. Vị trí ngồi của trường là khu vực gồm 4 hàng ghế, mỗi hàng có %s ghế.''' 
                             %(latex(n_students), latex(k_seats)))

            ########################################################################
            # Nhận biết (Hàng 1) ############################################
            # Đúng: A_n^k (vì học sinh và ghế đều phân biệt nên là chỉnh hợp)
            # Sai: C_n^k (chỉ là chọn học sinh, chưa xếp vào ghế)
            nb_da_1_d = '\\True Có $A_{%s}^{%s}$ cách sắp xếp %s bạn ngồi vào hàng ghế đầu tiên' %(latex(n_students), latex(k_seats), latex(k_seats))
            nb_da_1_s = 'Có $C_{%s}^{%s}$ cách sắp xếp %s bạn ngồi vào hàng ghế đầu tiên' %(latex(n_students), latex(k_seats), latex(k_seats))
            list_nb_da_1 = [nb_da_1_d, nb_da_1_s]
            nb_da_1 = random.choice(list_nb_da_1)

            list_nb_1 = [nb_da_1]
            loigiai_nb_1 = ('''Mỗi cách chọn %s học sinh từ %s học sinh và sắp xếp vào %s ghế ở hàng đầu tiên (có thứ tự) là một chỉnh hợp chập %s của %s. \\\\ Vậy có $A_{%s}^{%s}$ cách.''' 
                            %(latex(k_seats), latex(n_students), latex(k_seats), latex(k_seats), latex(n_students), latex(n_students), latex(k_seats)))

            list_nb_2 = [loigiai_nb_1]
            combined_nb = list(zip(list_nb_1, list_nb_2))
            random.shuffle(combined_nb)
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ########################################################################
            # Thông hiểu (Hàng 2) ############################################
            th_da_1_d = '\\True Sau khi sắp xếp xong hàng ghế đầu tiên, có $A_{%s}^{%s}$ cách sắp xếp %s bạn ngồi vào hàng ghế thứ hai' %(latex(n_con_lai_1), latex(k_seats), latex(k_seats))
            th_da_1_s = 'Sau khi sắp xếp xong hàng ghế đầu tiên, có $A_{%s}^{%s}$ cách sắp xếp %s bạn ngồi vào hàng ghế thứ hai' %(latex(n_students), latex(k_seats), latex(k_seats))
            list_th_da_1 = [th_da_1_d, th_da_1_s]
            th_da_1 = random.choice(list_th_da_1)

            list_th_1 = [th_da_1]
            loigiai_th_1 = ('''Sau hàng 1, còn lại $%s-%s=%s$ học sinh. Số cách xếp %s học sinh vào hàng 2 là $A_{%s}^{%s}$.''' 
                            %(latex(n_students), latex(k_seats), latex(n_con_lai_1), latex(k_seats), latex(n_con_lai_1), latex(k_seats)))

            list_th_2 = [loigiai_th_1]
            combined_th = list(zip(list_th_1, list_th_2))
            random.shuffle(combined_th)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ########################################################################
            # Vận dụng (Hàng 3) ############################################
            vd_da_1_d = '\\True Sau khi sắp xếp xong hàng ghế thứ hai, có $A_{%s}^{%s}$ cách sắp xếp %s bạn ngồi vào hàng ghế thứ ba' %(latex(n_con_lai_2), latex(k_seats), latex(k_seats))
            vd_da_1_s = 'Sau khi sắp xếp xong hàng ghế thứ hai, có $C_{%s}^{%s}$ cách sắp xếp %s bạn ngồi vào hàng ghế thứ ba' %(latex(n_con_lai_2), latex(k_seats), latex(k_seats))
            list_vd_da_1 = [vd_da_1_d, vd_da_1_s]
            vd_da_1 = random.choice(list_vd_da_1)

            list_vd_1 = [vd_da_1]
            loigiai_vd_1 = ('''Sau hàng 2, còn lại $%s-%s=%s$ học sinh. Số cách xếp %s học sinh vào hàng 3 là $A_{%s}^{%s}$.''' 
                            %(latex(n_con_lai_1), latex(k_seats), latex(n_con_lai_2), latex(k_seats), latex(n_con_lai_2), latex(k_seats)))

            list_vd_2 = [loigiai_vd_1]
            combined_vd = list(zip(list_vd_1, list_vd_2))
            random.shuffle(combined_vd)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)

            ########################################################################
            # Vận dụng cao (Hàng cuối) ############################################
            # Xếp n_con_lai_3 học sinh vào k_seats ghế (chọn ghế và xếp người)
            vdc_da_1_d = '\\True Sau khi sắp xếp xong hàng ghế thứ ba, có $A_{%s}^{%s}$ cách sắp xếp các bạn còn lại ngồi vào hàng ghế cuối cùng' %(latex(k_seats), latex(n_con_lai_3))
            vdc_da_1_s = 'Sau khi sắp xếp xong hàng ghế thứ ba, có $C_{%s}^{%s}$ cách sắp xếp các bạn còn lại ngồi vào hàng ghế cuối cùng' %(latex(k_seats), latex(n_con_lai_3))
            list_vdc_da_1 = [vdc_da_1_d, vdc_da_1_s]
            vdc_da_1 = random.choice(list_vdc_da_1)

            list_vdc_1 = [vdc_da_1]
            loigiai_vdc_1 = ('''Sau hàng 3, còn lại $%s$ học sinh. \\\\ Để xếp $%s$ học sinh vào hàng cuối có $%s$ ghế, ta chọn $%s$ ghế từ $%s$ ghế và sắp xếp $%s$ học sinh vào đó. \\\\ Số cách là $A_{%s}^{%s}$.''' 
                             %(latex(n_con_lai_3), latex(n_con_lai_3), latex(k_seats), latex(n_con_lai_3), latex(k_seats), latex(n_con_lai_3), latex(k_seats), latex(n_con_lai_3)))

            list_vdc_2 = [loigiai_vdc_1]
            combined_vdc = list(zip(list_vdc_1, list_vdc_2))
            random.shuffle(combined_vdc)
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

            # Xuất câu hỏi
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

