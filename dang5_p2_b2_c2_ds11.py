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


def bt_dang5_p2_b2_c2_ds11(self):
            # Khai báo biến
            # Random cạnh hình vuông ban đầu 'a' là một số nguyên từ 1 đến 5.
            a = randint(1,10) 
            S1 = a**2           # Diện tích hình vuông ban đầu (S1)
            S_total = S1 * 2    # Tổng diện tích vô hạn (2 * S1)
            q = Rational(1, 2)  # Công bội luôn là 1/2

            # Nội dung câu hỏi
            noidungcauhoi = ('''Từ hình vuông có độ dài cạnh $a_1=%s$ (hình minh họa), người ta nối các trung điểm của cạnh hình vuông để tạo ra hình vuông mới. Tiếp tục quá trình này đến vô hạn.\\\\ \n'''
                             '''\\begin{center}
                             \\begin{tikzpicture}[line cap=round,line join=round,>=triangle 45,x=1cm,y=1cm]
            	\\clip(-0.1,-0.1) rectangle (4.1,4.1);
            	\\draw [line width=1.2pt] (0,0)-- (0,4);
            	\\draw [line width=1.2pt] (0,4)-- (4,4);
            	\\draw [line width=1.2pt] (4,4)-- (4,0);
            	\\draw [line width=1.2pt] (4,0)-- (0,0);
            	\\draw [line width=1.2pt] (0,2)-- (2,4);
            	\\draw [line width=1.2pt] (2,4)-- (4,2);
            	\\draw [line width=1.2pt] (4,2)-- (2,0);
            	\\draw [line width=1.2pt] (2,0)-- (0,2);
            	\\draw [line width=1.2pt] (1,3)-- (3,3);
            	\\draw [line width=1.2pt] (3,3)-- (3,1);
            	\\draw [line width=1.2pt] (3,1)-- (1,1);
            	\\draw [line width=1.2pt] (1,1)-- (1,3);
            	\\draw [line width=1.2pt] (2,3)-- (1,2);
            	\\draw [line width=1.2pt] (1,2)-- (2,1);
            	\\draw [line width=1.2pt] (2,1)-- (3,2);
            	\\draw [line width=1.2pt] (3,2)-- (2,3);
            	\\draw [line width=1.2pt] (1.5,2.5)-- (2.5,2.5);
            	\\draw [line width=1.2pt] (2.5,2.5)-- (2.5,1.5);
            	\\draw [line width=1.2pt] (2.5,1.5)-- (1.5,1.5);
            	\\draw [line width=1.2pt] (1.5,1.5)-- (1.5,2.5);
            	\\draw [line width=1.2pt] (1.5,2)-- (2,2.5);
            	\\draw [line width=1.2pt] (2,2.5)-- (2.5,2);
            	\\draw [line width=1.2pt] (2.5,2)-- (2,1.5);
            	\\draw [line width=1.2pt] (2,1.5)-- (1.5,2);
            \\end{tikzpicture}
                             \\end{center}'''
                            %(latex(a)))

            ######################################################################## Nhận biết (Tính S1) ############################################

            # Đáp án đúng
            nb_da_1_d = '\\True Diện tích hình vuông ban đầu ($n=1$) là $%s$' %(latex(S1))
            # Đáp án sai: S1 + 1 (hoặc S1 + 2 nếu S1=1)
            nb_da_1_s = 'Diện tích hình vuông ban đầu ($n=1$) là $%s$' %(latex(S1 + 1 if a > 1 else S1 + 2)) 
            list_nb_da_1=[nb_da_1_d,nb_da_1_s]
            # Lời giải
            loigiai_nb_1 = ('''Diện tích hình vuông ban đầu là $S_1=a_1^2=%s^2=%s$.''' %(latex(a), latex(S1)))
            list_nb_2 = [loigiai_nb_1]

            ########################################################################Thông hiểu (Công bội) ############################################
            # Đáp án đúng
            th_da_1_d = '\\True Dãy diện tích $(S_n)$ là cấp số nhân với công bội $q=%s$' %(latex(q))
            # Đáp án sai: q = 1/4 (thường bị nhầm lẫn)
            th_da_1_s = 'Dãy diện tích $(S_n)$ là cấp số nhân với công bội $q=%s$' %(latex(Rational(1, 4))) 
            list_th_da_1=[th_da_1_d,th_da_1_s]
            # Lời giải
            loigiai_th_1 = ('''Hình vuông sau luôn có diện tích bằng $\\frac{1}{2}$ hình vuông trước. Do đó, dãy diện tích $(S_n)$ là cấp số nhân với công bội $q=\\frac{1}{2}$.''' )
            list_th_2 = [loigiai_th_1]

            ######################################################################## Vận dụng (Công thức Sn) ############################################
            # Đáp án đúng
            vd_da_1_d = '\\True Diện tích hình vuông ở bước $n$ là $S_n=%s \\cdot \\left( %s \\right)^{n-1}$' %(latex(S1), latex(q))
            # Đáp án sai: Thiếu S1 (chỉ lấy q^(n-1))
            vd_da_1_s = 'Diện tích hình vuông ở bước $n$ là $S_n=\\left( %s \\right)^{n-1}$' %(latex(q)) 
            list_vd_da_1=[vd_da_1_d,vd_da_1_s]
            # Lời giải
            loigiai_vd_1 = ('''Áp dụng công thức tổng quát của cấp số nhân: $S_n = S_1 \\cdot q^{n-1} = %s \\cdot \\left(\\frac{1}{2}\\right)^{n-1}$.'''
                        %(latex(S1)))
            list_vd_2 = [loigiai_vd_1]

            ######################################################################## Vận dụng cao (Tổng vô hạn S) ############################################
            # Đáp án đúng
            vdc_da_1_d = '\\True Tổng diện tích tất cả các hình vuông (đến vô hạn) là $%s$' %(latex(S_total))
            # Đáp án sai: Chỉ lấy S1
            vdc_da_1_s = 'Tổng diện tích tất cả các hình vuông (đến vô hạn) là $%s$' %(latex(S1)) 
            list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
            # Lời giải
            loigiai_vdc_1 = ('''Tổng diện tích là tổng của cấp số nhân lùi vô hạn ($|q|<1$):
                        $S = \\frac{S_1}{1-q} = \\frac{%s}{1-\\frac{1}{2}} = \\frac{%s}{\\frac{1}{2}} = %s$.'''
                        %(latex(S1), latex(S1), latex(S_total)))
            list_vdc_2 = [loigiai_vdc_1]


            ######################################################################## Logic chọn và xáo trộn ############################################

            def count_true_answers(answers):
                # Hàm đếm số đáp án đúng
                return sum('\\True' in ans for ans in answers)

            # Lặp đến khi 4 đáp án có từ 1 đến 3 đúng
            while True:
                nb_da_1 = random.choice(list_nb_da_1)
                th_da_1 = random.choice(list_th_da_1)
                vd_da_1 = random.choice(list_vd_da_1)
                vdc_da_1 = random.choice(list_vdc_da_1)
                answers = [nb_da_1, th_da_1, vd_da_1, vdc_da_1]
                true_count = count_true_answers(answers)
                if 1 <= true_count <= 3:
                    break

            # Gán lại vào list (đảm bảo đáp án được chọn ngẫu nhiên)
            list_nb_1 = [nb_da_1]
            list_th_1 = [th_da_1]
            list_vd_1 = [vd_da_1]
            list_vdc_1 = [vdc_da_1]

            # Kết hợp đáp án và lời giải cho từng cấp độ
            combined_nb = list(zip(list_nb_1, list_nb_2))
            combined_th = list(zip(list_th_1, list_th_2))
            combined_vd = list(zip(list_vd_1, list_vd_2))
            combined_vdc = list(zip(list_vdc_1, list_vdc_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_nb)
            random.shuffle(combined_th)
            random.shuffle(combined_vd)
            random.shuffle(combined_vdc)

            # Tách lại danh sách đã xáo trộn
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)
            shuffled_answers_vd, shuffled_solutions_vd = zip(*combined_vd)
            shuffled_answers_vdc, shuffled_solutions_vdc = zip(*combined_vdc)

            # Xuất câu hỏi với đáp án và lời giải đã được xáo trộn
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

