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


def bt_dang2_p2_b1_c1_ds11(self):
            # Khai báo biến
            lis=[pi/6,pi/4,pi/3,2*pi/3,3*pi/4,5*pi/6]
            a=random.choice(lis)
            g=a*180/pi

            r=randint(2,20)

            lis1=[2,3,4,5,6,7,8,9,-2,-3,-4,-5,-6,-7,-8,-9]
            a1=random.choice(lis1)
            lis1.remove(a1)
            b1=random.choice(lis1)
            lis1.remove(b1)
            a2=random.choice(lis1)
            lis1.remove(a2)
            b2=random.choice(lis1)
            kq=(a1*tan(a)+b1*tan(a))/(a2*tan(a)+b2*tan(a))
            # Nội dung câu hỏi
            noidungcauhoi = ('''Cho góc lượng giác $\\alpha =%s$.'''                 
                            %(latex(a)
                                ))

            ######################################################################## Nhận biết ############################################
            # Các đáp án
            nb_da_1_d = '\\True Số đo góc $\\alpha$ đổi sang đơn vị độ là $%s^\\circ$' %(latex(g))
            nb_da_1_s = 'Số đo góc $\\alpha$ đổi sang đơn vị độ là $%s^\\circ$' %(latex(180-g))
            list_nb_da_1=[nb_da_1_d,nb_da_1_s]
            nb_da_1=random.choice(list_nb_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_nb_1 = [nb_da_1]

            # Nội dung lời giải
            loigiai_nb_1 = ('''Số đo góc $\\alpha$ đổi sang đơn vị độ là $\\alpha = %s \\frac{180}{\\pi}=%s^\\circ$.'''
                        %(latex(a),latex(g)
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
            th_da_1_d = '\\True $\\tan \\alpha =%s$' %(latex(tan(a)))  
            th_da_1_s = '$\\tan \\alpha =%s$' %(latex(cos(a))) 
            list_th_da_1=[th_da_1_d,th_da_1_s]
            th_da_1=random.choice(list_th_da_1)

            th_da_2_d = '\\True $\\cot \\alpha =%s$' %(latex(cot(a)))  
            th_da_2_s = '$\\cot \\alpha =%s$' %(latex(sin(a))) 
            list_th_da_2=[th_da_2_d,th_da_2_s]
            th_da_2=random.choice(list_th_da_2)

            th_da_3_d = '\\True $\\sin \\alpha =%s$' %(latex(sin(a)))  
            th_da_3_s = '$\\sin \\alpha =%s$' %(latex(tan(a))) 
            list_th_da_3=[th_da_3_d,th_da_3_s]
            th_da_3=random.choice(list_th_da_3)

            th_da_4_d = '\\True $\\cos \\alpha =%s$' %(latex(cos(a)))  
            th_da_4_s = '$\\cos \\alpha =%s$' %(latex(tan(a))) 
            list_th_da_4=[th_da_4_d,th_da_4_s]
            th_da_4=random.choice(list_th_da_4)
            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_th_1 = [th_da_1,th_da_2,th_da_3,th_da_4]

            # Nội dung lời giải
            loigiai_th_1 = ('''Ta có $\\tan \\alpha =%s$.'''       
                        %(latex(tan(a))
                            ))
            loigiai_th_2 = ('''Ta có $\\cot \\alpha =%s$.'''       
                        %(latex(cot(a))
                            ))
            loigiai_th_3 = ('''Ta có $\\sin \\alpha =%s$.'''       
                        %(latex(sin(a))
                            ))
            loigiai_th_3 = ('''Ta có $\\cos \\alpha =%s$.'''       
                        %(latex(cos(a))
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
            vd_da_1_d = '\\True Biết cung tròn ứng với góc $\\alpha$ có bán kính $R=%s$ cm. Độ dài cung là $%s$ cm' %(latex(r),latex(r*a))  
            vd_da_1_s = 'Biết cung tròn ứng với góc $\\alpha$ có bán kính $R=%s$ cm. Độ dài cung là $%s$ cm' %(latex(r),latex((r+1)*a))   
            list_vd_da_1=[vd_da_1_d,vd_da_1_s]
            vd_da_1=random.choice(list_vd_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vd_1 = [vd_da_1]

            # Nội dung lời giải
            loigiai_vd_1 = ('''Độ dài cung của góc $\\alpha$ là $l=R \\cdot \\alpha=%s \\cdot %s =%s$ cm.'''  
                        %(latex(r),latex(a),latex(r*a)
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
            vdc_da_1_d = '\\True Giá trị $P=\\frac{%s \\sin \\alpha+%s \\cos \\alpha}{%s \\sin \\alpha+%s \\cos \\alpha}$ bằng $%s$' %(latex(a1),latex(b1),latex(a2),latex(b2),latex(kq)) 
            vdc_da_1_s = 'Giá trị $P=\\frac{%s \\sin \\alpha+%s \\cos \\alpha}{%s \\sin \\alpha+%s \\cos \\alpha}$ bằng $%s$' %(latex(a1),latex(b1),latex(a2),latex(b2),latex(kq+1)) 
            list_vdc_da_1=[vdc_da_1_d,vdc_da_1_s]
            vdc_da_1=random.choice(list_vdc_da_1)

            # Đưa các đáp án vào 1 danh sách chọn ngẫu nhiên
            list_vdc_1 = [vdc_da_1]

            # Nội dung lời giải
            loigiai_vdc_1 = ('''Ta có $\\tan \\alpha =%s$, khi đó \\\\
                            $P=\\frac{%s \\sin \\alpha+%s \\cos \\alpha}{%s \\sin \\alpha+%s \\cos \\alpha}=\\frac{%s \\tan \\alpha+%s}{%s \\tan \\alpha+%s}=%s$.'''
                        %(latex(tan(a)),
                        latex(a1),latex(b1),latex(a2),latex(b2),
                        latex(a1),latex(b1),latex(a2),latex(b2),latex(kq)
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
                '\\end{ex}\n \\end{minipage} \n\n').replace('+-', '-')
            return content

