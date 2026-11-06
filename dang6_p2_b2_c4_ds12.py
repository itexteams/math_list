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


def bt_dang6_p2_b2_c4_ds12(self):
            # Khai báo biến
            a=randint(40,50)
            pa=a/100
            p_a=1-pa

            b=100-a
            pb=b/100
            p_b=round(1-pb,2)


            c=randint(3,4)
            pc=c/100
            p_c=1-pc

            d=randint(1,2)
            pd=d/100
            p_d=1-pd

            pe=pa*pc+pb*pd

            pba=round(pa*pc/pe,2)


            kq=1-pba
            h1=kq   
            number = Decimal(float(h1))  # Số cần làm tròn
            kqz = number.quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)

            # Nội dung câu hỏi
            noidungcauhoi = ('Một nhà máy có hai phân xưởng I và IIzz Phân xưởng I sản xuất $%s$phtr số sản phẩm và phân xưởng II sản xuất $%s$phtr số sản phẩmzz Tỉ lệ sản phẩm bị lỗi của phân xưởng I là $%s$phtr và của phân xưởng II là $%s$phtrzz Kiểm tra ngẫu nhiên một sản phẩm của nhà máyzz'
                            %(latex(a),latex(b),latex(c),latex(d)
                            ))

            ######################################################################## Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True Xác suất sản phẩm được kiểm tra do phân xưởng II sản xuất là $%s$' %(latex(p_a))
            nb_da_1_s = 'Xác suất sản phẩm được kiểm tra do phân xưởng II sản xuất là $%s$' %(latex(pa))
            list_nb_da_1=[nb_da_1_d,nb_da_1_s]
            nb_da_1=random.choice(list_nb_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = ('Gọi các biến cố: \\\\ \n'
                    '\\hspace*{1cm} $A$:"Sản phẩm được kiểm tra bị lỗi"zz \\\\ \n'
                    '\\hspace*{1cm} $B$:"Sản phẩm được kiểm tra do phân xưởng I sản xuất"zz \\\\ \n'
                    'Do phân xưởng I sản xuất $%s$phtr số sản phẩm và phân xưởng II sản xuất $%s$phtr số sản phẩm nên \n'
                    '$$P(B)=%s \\hspace*{0zz5cm} \\text{và} \\hspace*{0zz5cm} P(\\overline{B})=1-%s=%szz$$'
                    %(latex(a),latex(b),               
                    latex(pa),latex(pa),latex(p_a),
                        ))

            # Đưa các lời giải vào danh sách lời giải
            list_nb_2 = [loigiai_nb_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_nb = list(zip(list_nb_1, list_nb_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_nb)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_nb, shuffled_solutions_nb = zip(*combined_nb)

            ######################################################################## Thông hiểu ############################################
            # Các đáp án
            th_da_1_d = '\\True Xác suất sản phẩm được kiểm tra bị lỗi của phân xưởng II là $%s$' %(latex(pd))
            th_da_1_s = 'Xác suất sản phẩm được kiểm tra bị lỗi của phân xưởng II là $%s$' %(latex(p_d))
            list_th_da_1=[th_da_1_d,th_da_1_s]
            th_da_1=random.choice(list_th_da_1)


            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1]

            # Nội dung lời giải
            loigiai_th_1 = ('Do tỉ lệ sản phẩm bị lỗi của phân xưởng I là $%s$phtr và của phân xưởng II là $%s$phtr nên \n'
            '$$P(A|B)=%s \\hspace*{0zz5cm} \\text{và} \\hspace*{0zz5cm} P(A| \\overline{B})=%szz$$'
                        %(latex(c),latex(d),
                        latex(pc),latex(pd),
                            ))


            # Đưa các lời giải vào danh sách lời giải
            list_th_2 = [loigiai_th_1]

            # Kết hợp các đáp án và lời giải vào cùng một danh sách
            combined_th = list(zip(list_th_1, list_th_2))

            # Xáo trộn danh sách kết hợp
            random.shuffle(combined_th)

            # Tách lại danh sách đã xáo trộn thành các danh sách đáp án và lời giải
            shuffled_answers_th, shuffled_solutions_th = zip(*combined_th)

            ######################################################################## Vận dụng ############################################
            # Các đáp án
            vd_da_1_d = '\\True Xác suất để một sản phẩm được kiểm tra bị lỗi là $%s$' %(latex(pe))  
            vd_da_1_s = 'Xác suất để một sản phẩm được kiểm tra bị lỗi là $%s$' %(latex(1-pe))    
            list_vd_da_1=[vd_da_1_d,vd_da_1_s]
            vd_da_1=random.choice(list_vd_da_1)


            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            loigiai_vd_1 = (

                'Xác xuất để một sản phẩm được kiểm tra bị lỗi là \n'
                '$$P(A)=P(B) P(A|B)+P(\\overline{B}) P(A| \\overline{B})=%s \\cdot %s +%s \\cdot %s=%szz$$'


                        %(
                        latex(pa),latex(pc),latex(pb),latex(pd),latex(pe),

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
            vdc_da_1_d = '\\True Xác suất sản phẩm kiểm tra bị lỗi của phân xưởng II là $%s$' %(latex(kqz))  
            vdc_da_1_s = 'Xác suất sản phẩm kiểm tra bị lỗi của phân xưởng II là $%s$' %(latex(1-kq))  
            list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
            vdc_da_1=random.choice(list_vdc_da_1)


            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải
            loigiai_vdc_1 = (
                        'Nếu sản phẩm được kiểm tra bị lỗi thì xác suất sản phẩm đó do phân xưởng I sản xuất là \n'
                        '$$P(B|A)=\\dfrac{P(B) P(A|B)}{P(A)}=\\dfrac{%s \\cdot %s}{%s}=%szz$$ \n'
                        'Nếu sản phẩm được kiểm tra bị lỗi thì xác suất sản phẩm đó do phân xưởng II sản xuất là \n'
                        '$$P(\\overline{B}|A)=1-P(B|A)=1-%s=%szz$$'
                        %( latex(pa),latex(pc),latex(pe),latex(pba),
                        latex(pba),latex(kqz)
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
                '\\end{ex}\n \\end{minipage} \n\n').replace('\\frac', '\\dfrac').replace('.', ',').replace('zz', '.').replace('phtr', '\\%')
            return content

